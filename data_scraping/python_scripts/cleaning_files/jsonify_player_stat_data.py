import pandas as pd
import json

df = pd.read_csv(r"C:\Users\Devin Diaz\OneDrive\Desktop\Github-Projects\Egoist-Engine\scraping_data\python_scripts\cleaning_files\player_stats.csv")

def convert_to_json(value):
    if pd.isna(value) or value == '':
        return None
    if value.startswith('[') and value.endswith(']'):
        return json.dumps(value[1:-1].split(','))
    return json.dumps(value)

df['weapon'] = df['weapon'].apply(convert_to_json)

print(df.head())