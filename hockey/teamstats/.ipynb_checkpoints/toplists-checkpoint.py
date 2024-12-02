#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import pkg_resources

def TopTeams():
    year = input("Enter the season you would like data for: Please just enter the year the season finished (e.g., 2021/2022 enter 2022)")

    csv_filename = f"Team{year}.csv"
    
    csv_path = pkg_resources.resource_stream(__name__, f"../{csv_filename}")
        
    TeamData = pd.read_csv(csv_path)

    num_teams = int(input("Enter the number of top teams you want to display: "))
    
    top_teams = TeamData[['Team', 'PTS']].sort_values(by='PTS', ascending=False).head(num_teams)
    
    return top_teams

def TopAssists():
    year = input("Enter the season you would like data for: Please just enter the year the season finished (e.g., 2021/2022 enter 2022)")

    csv_filename = f"skaters{year}.csv"
    
    csv_path = pkg_resources.resource_stream(__name__, f"../player/data/{csv_filename}")
        
    skaterData = pd.read_csv(csv_path)

    num_players = int(input("Enter the number of players you want to display: "))

    filtered_data = skaterData[skaterData['situation'] == 'all']

    top_players = filtered_data[['name', 'I_F_primaryAssists', 'I_F_secondaryAssists']] \
                      .assign(total_assists=filtered_data['I_F_primaryAssists'] + filtered_data['I_F_secondaryAssists']) \
                      .sort_values(by='total_assists', ascending=False) \
                      .head(num_players)
    
    return top_players

def TopGoals():
    year = input("Enter the season you would like data for: Please just enter the year the season finished (e.g., 2021/2022 enter 2022)")

    csv_filename = f"skaters{year}.csv"
    
    csv_path = pkg_resources.resource_stream(__name__, f"../player/data/{csv_filename}")
        
    skaterData = pd.read_csv(csv_path)

    num_players = int(input("Enter the number of players you want to display: "))

    filtered_data = skaterData[skaterData['situation'] == 'all']

    top_players = filtered_data[['name', 'I_F_goals']].sort_values(by='I_F_goals', ascending=False).head(num_players)
    
    return top_players