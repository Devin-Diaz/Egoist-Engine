import pandas as pd
import requests
from bs4 import BeautifulSoup

# IGNORE ONLY FOR TESTING PURPOSES
MOCK_DATA_FOR_TESTING = [
    'https://bluelock.fandom.com/wiki/Picasso',
    'https://bluelock.fandom.com/wiki/Burai_Daido',  
    'https://bluelock.fandom.com/wiki/Kenyu_Yukimiya',   
    'https://bluelock.fandom.com/wiki/Haruhiko_Yuzu',    
    'https://bluelock.fandom.com/wiki/Ikki_Niko'
]

# IGNORE, WERE USED FOR TESTING AND DEBUGGING
def display_set(hashset):
    for link in hashset:
        print(link)

def display_list(content):
    for player in content:
        print(player)


# Blue lock wiki where I got all my data from. Don't sue me pls I just want internship.
MAIN_URL = 'https://bluelock.fandom.com/wiki/List_of_Characters'

# Keeps track of all players in the blue lock database. Primary key for general player data
player_id_counter = 1

# ensures we get a status 200 on every page link we retreive when we want to parse
def test_url_request(url) -> requests:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f'ERROR OCCURED: {e}')
        return


# determines if a blue lock character is actually a player based on keywords in their wiki profile
def is_player(character_link) -> bool:
    response = test_url_request(character_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    keywords = ['Jersey Number(s)', 'Weapon']
    profile_data = soup.find_all('h3', class_='pi-data-label pi-secondary-font')

    for label in profile_data:
        label_text = label.text.strip()
        if label_text in keywords: return True

    return False


# Scrapes all hrefs of each player page on the main page. 
# We need each href to examine each players data individually. 
def get_character_hrefs() -> set[str]:
    response = test_url_request(MAIN_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    character_links = set()
    tables = soup.find_all('table')

    for table in tables:
        links = table.find_all('a', href=True, title=True)
        for link in links:
            href = link['href']
            if href.startswith('/wiki/'):
                full_url = 'https://bluelock.fandom.com' + href
                if is_player(full_url):
                    character_links.add(full_url)
    return character_links


# Little helper functions to ensure scraped height and age data is correct type and format
def parse_players_height(height: str) -> str:
    parsed_height = height.split()
    return f'{parsed_height[0]} cm'

def parse_players_age(age: str) -> int:
    parsed_age = age[0:2]
    return int(parsed_age)
    

# Examines a single players wiki profile and scrapes, full name, age, height, nation, 
# and profile image via dictionary. If nothing is found, value will default to null. 
def scrape_player_general_data(character_link) -> dict:
    global player_id_counter
    response = test_url_request(character_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    player_dict = {'player_id': player_id_counter, 'full_name': None, 'age': None, 'height': None, 'nationality': None, 'image': None}

    profile_labels = soup.find_all('h3', class_='pi-data-label pi-secondary-font')    

    name_details = soup.find('span', class_='mw-page-title-main')
    player_dict['full_name'] = name_details.text.strip()

    for label in profile_labels:
        label_text = label.text.strip()
        value_div = label.find_next_sibling('div')
        value_text = value_div.text.strip()
        if label_text == 'Age': player_dict['age'] = parse_players_age(value_text)
        elif label_text == 'Height': player_dict['height'] = parse_players_height(value_text)
        elif label_text == 'Affiliation': player_dict['nationality'] = value_text
    
    image_details = soup.find('figure', class_='pi-item pi-image')
    img_tag = image_details.find('img')
    if img_tag and img_tag.get('src'):
        player_dict['image'] = img_tag['src']
    
    player_id_counter += 1
    return player_dict

# Iterates through every player wiki profile and scrapes needed details from function above. 
# Each player entry (dict) gets appened to one big list.
def scrape_all_player_general_data() -> list[dict]:
    player_data = []
    player_hrefs = get_character_hrefs()
    for player_page in player_hrefs:
        player_dict = scrape_player_general_data(player_page)
        player_data.append(player_dict)
    return player_data


# Converting list of player data to dataframe
ALL_PLAYER_DATA = scrape_all_player_general_data()
players_df = pd.DataFrame(ALL_PLAYER_DATA)

# Saving dataframe to csv file
players_df.to_csv('players.csv', index=False)

