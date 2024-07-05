import pandas as pd
import requests
from bs4 import BeautifulSoup
from player_hrefs_data_loader import PLAYER_HREFS
from arc_and_team_data_loader import ARC_DATA, TEAM_DATA

# will be used as the id for each stat entry
stat_counter = 1

# Getting player id and full name from player general data csv file. The purpose is we will use full name to track down our id
# when creating an entry for player stat.
PLAYER_CSV_FILE = r"C:\Users\Devin Diaz\OneDrive\Desktop\Github-Projects\Egoist-Engine\scraping_data\csv_files\players.csv"
columns = ['player_id', 'full_name']
player_dataframe = pd.read_csv(PLAYER_CSV_FILE, usecols=columns)


# ensures we get a status 200 on every page link we retreive when we want to parse (could've imported but didn't want unnecessary complications)
def test_url_request(url) -> requests:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f'ERROR OCCURED: {e}')
        return

# Scrapes name of player, With the name we can use that to find the tuple of that player in the general player dataframe.
# We can then use the index and the name of the column to find the value of the correct player id 
def retrieve_player_id(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    character_name = soup.find('span', class_='mw-page-title-main')

    name = character_name.text.strip()
    index_list = player_dataframe.index[player_dataframe['full_name'] == name].to_list()
    index = index_list[0]
    player_id = player_dataframe.iloc[index]['player_id']
    return int(player_id)


def retrieve_arc_and_team_id(response):
    soup = BeautifulSoup(response.content, 'html.parser')



def scrape_stat_data(character_link):
    global stat_counter
    response = test_url_request(character_link)
    stat_dict = {'player_stat_id': stat_counter, 'player_id': None, 'arc_id': None, 
                 'team_id': None, 'position': None, 'weapon': None, 'jersey_no': None}
    
    player_id = retrieve_player_id(response)
    stat_dict['player_id'] = player_id

    print(stat_dict)


    stat_counter += 1



scrape_stat_data('https://bluelock.fandom.com/wiki/Tabito_Karasu')
