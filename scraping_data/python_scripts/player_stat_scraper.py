import json
import re
from collections import defaultdict
import pandas as pd
import requests
from bs4 import BeautifulSoup
from player_hrefs_data_loader import PLAYER_HREFS
from arc_and_team_data_loader import ARC_DATA, TEAM_DATA

#---------------------------------------------------------------------------------------------------------------------------
# will be used as the id for each stat entry
stat_id_counter = 1
#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# CSV DATA FROM OTHER TABLES TO ENSURE FOREIGN KEYS ARE ACCURATE IN PLAYER STAT CSV FILE

# Getting player id and full name from player general data csv file. The purpose is we will use full name to track down our id
# when creating an entry for player stat.
PLAYER_CSV_FILE = r"C:\Users\Devin Diaz\OneDrive\Desktop\Github-Projects\Egoist-Engine\scraping_data\csv_files\players.csv"
player_dataframe = pd.read_csv(PLAYER_CSV_FILE, usecols=['player_id', 'full_name'])

TEAMS_CSV_FILE = r"C:\Users\Devin Diaz\OneDrive\Desktop\Github-Projects\Egoist-Engine\scraping_data\csv_files\teams.csv"
teams_df = pd.read_csv(TEAMS_CSV_FILE, usecols=['team_id', 'arc_id', 'team_name'])

TEAM_NAMES = teams_df['team_name'].tolist()

#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# USED TO ENSURE THE PAGE WE WANT TO SCRAPE FROM ACTUALLY EXISTS
# ensures we get a status 200 on every page link we retreive when we want to parse (could've imported but didn't want unnecessary complications)
def test_url_request(url) -> requests:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f'ERROR OCCURED: {e}')
        return
#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# GETS THE PLAYER ID FROM PLAYER GENERAL DATA CSV
# Scrapes name of player, With the name we can use that to find the tuple of that player in the general player dataframe.
# We can then use the index and the name of the column to find the value of the correct player id 
def retrieve_player_id(response) -> int:
    soup = BeautifulSoup(response.content, 'html.parser')
    character_name = soup.find('span', class_='mw-page-title-main')

    name = character_name.text.strip()
    index_list = player_dataframe.index[player_dataframe['full_name'] == name].to_list()
    index = index_list[0]
    player_id = player_dataframe.iloc[index]['player_id']
    return int(player_id)
#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# FORMATS THE STRINGS FOR EACH TEAM TO ENSURE THEY APPEAR AS THEY DO IN OTHER CSV FILES
# Returns a players current team if he has one
def parse_player_current_team(team_text: str) -> str:
    parsed_word = ''
    for c in team_text:
        if c =='(': break
        parsed_word += c
    return str(parsed_word.strip())

# Returns a set of all former teams of a player
def parse_player_former_teams(former_team_text: str) -> set[str]:
    former_teams = set()
    split_by_bracket_arr = former_team_text.split(']')
    for entry in split_by_bracket_arr:
        team = ''
        for c in entry:
            if c == '(' or c == '[':
                break
            team += c
        former_teams.add(team.strip())

    return set(filter(None, former_teams))
#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# RETURNS ALL TEAMS A PLAYER HAS PLAYED ON IN PROPER FORMAT
# Will return a list of a player's current team and former teams in string format
def retrieve_all_player_teams(response) -> set[str]:
    all_teams = set()
    soup = BeautifulSoup(response.content, 'html.parser')
    profile_labels = soup.find_all('h3', class_='pi-data-label pi-secondary-font')

    for label in profile_labels:
        label_text = label.text.strip()
        value_div = label.find_next_sibling('div')
        value_text = value_div.text.strip()
        if label_text == 'Team': 
            current_team = parse_player_current_team(value_text)
            if current_team in TEAM_NAMES:
                all_teams.add(current_team)
        elif label_text == 'Former team(s)':
            former_teams = parse_player_former_teams(value_text)
            all_teams.update(team for team in former_teams if team in TEAM_NAMES)
    
    if 'Team Blue Lock' in all_teams:
        all_teams.remove('Team Blue Lock')
    return all_teams
#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# GETS THE TEAM AND ARC ID FOR ANY EXISTING TEAM
# A team will get passed into this function and return the team id in the first element, and arc id in second. 
def retrieve_arc_and_team_id(team_name: str) -> list[int]:
    index_list = teams_df.index[teams_df['team_name'] == team_name].to_list()
    index = index_list[0]
    team_id = teams_df.iloc[index]['team_id']
    arc_id = teams_df.iloc[index]['arc_id']
    return [team_id, arc_id]
#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# UPDATED FUNCTION TO PARSE JERSEY NUMBERS
def parse_jersey_numbers(jersey_str: str) -> list[int]:
    # Use regex to find all numbers, both within and outside parentheses
    numbers = re.findall(r'\b\d+\b', jersey_str)
    return [int(number) for number in numbers]

def retrieve_all_jersey_numbers(response):
    all_jerseys = []
    soup = BeautifulSoup(response.content, 'html.parser')
    profile_labels = soup.find_all('h3', class_='pi-data-label pi-secondary-font')
    for label in profile_labels:
        label_text = label.text.strip()
        value_div = label.find_next_sibling('div')
        value_text = value_div.text.strip()
        if label_text == 'Jersey Number(s)': all_jerseys += parse_jersey_numbers(value_text)
    return all_jerseys

#---------------------------------------------------------------------------------------------------------------------------


# Example function to convert a list to a JSON string representation
def convert_list_to_json_str(lst):
    return json.dumps(lst)

#---------------------------------------------------------------------------------------------------------------------------
# RETURNS COMPLETE DATA ENTRY DICTIONARIES FOR A PLAYER DEPENDING HOW MANY TEAMS THEY HAVE PLAYED
# Will return a dict of stats for each team a player has played on
def scrape_stat_data(character_link):
    global stat_id_counter
    all_player_team_stats = []
    response = test_url_request(character_link)
    
    player_id = retrieve_player_id(response)
    all_teams = retrieve_all_player_teams(response)
    all_jersey_nums = retrieve_all_jersey_numbers(response)
    print(all_jersey_nums)

    for team in all_teams:
        team_arc_data = retrieve_arc_and_team_id(team)
        team_id = int(team_arc_data[0])
        arc_id = int(team_arc_data[1])
        
        stat_dict = defaultdict(lambda: None)
        stat_dict.update({'player_stat_id': stat_id_counter, 
                          'player_id': player_id, 
                          'arc_id': arc_id, 
                          'team_id': team_id, 
                          'jersey_no': convert_list_to_json_str(all_jersey_nums),
                          'weapon': None,
                          'position': None})

        all_player_team_stats.append(dict(stat_dict))
        stat_id_counter += 1
    
    return all_player_team_stats
    
#---------------------------------------------------------------------------------------------------------------------------

# COLLECTING ALL PLAYER STATS
ALL_PLAYER_STATS = []
for player_href in PLAYER_HREFS:
    player_stats = scrape_stat_data(player_href)
    ALL_PLAYER_STATS += player_stats

# # CONVERTING TO CSV FILE
player_stats_df = pd.DataFrame(ALL_PLAYER_STATS)

# Saving dataframe to csv file
player_stats_df.to_csv('player_stats.csv', index=False)
