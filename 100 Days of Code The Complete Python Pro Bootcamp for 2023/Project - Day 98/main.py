import pandas as pd



def clean_data(df):

# Drop duplicate rows across all columns

df = df.drop_duplicates()

# Drop column: 'Unnamed: 0.1'

df = df.drop(columns=['Unnamed: 0.1'])

# Drop column: 'Unnamed: 0'

df = df.drop(columns=['Unnamed: 0'])

# Sort by column: 'Organisation' (ascending)

df = df.sort_values(['Organisation'])

# Sort by column: 'Organisation' (descending)

df = df.sort_values(['Organisation'], ascending=[False])

return df



# Loaded variable 'df' from URI: /Users/williethomas/Desktop/Space+Missions+(start)/mission_launches.csv

df = pd.read_csv(r"/Users/williethomas/Desktop/Space+Missions+(start)/mission_launches.csv")



df_clean = clean_data(df.copy())

df_clean.head()