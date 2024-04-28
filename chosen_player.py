import random
import pandas as pd


def player():
    data= pd.read_csv('output.csv')  #here we take the input from the dataset which we created of players
    player_list = data['Player_Name'].tolist()
    #print(player_list)
    chosen_player = random.choice(player_list).lower().strip()
    #print(chosen_player)
    return chosen_player
