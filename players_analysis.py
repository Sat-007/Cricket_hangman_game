import pandas as pd
data = pd.read_csv('cricket_data.csv') #dataset of all cricketers
df = data.loc[:, ['Player_Name']]  #consider only player_names and not rest of the cols
df.drop_duplicates(inplace = True)
df.to_csv('output.csv')