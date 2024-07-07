import pandas as pd

# Read the csv file
df = pd.read_csv('players.csv')

# Set 'nationality' to 'Japan' where it is blank. (not ideal)
df['nationality'].fillna('Japan', inplace=True)

# Remove the '.0' from 'age' values
df['age'] = df['age'].apply(lambda x: str(x).replace('.0', '') if pd.notnull(x) else x)

# Save the modified dataframe back to csv
df.to_csv('players_updated.csv', index=False)

print('csv file has been updated.')