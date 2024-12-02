#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pkg_resources

def LoadData():
    year = input("Enter the season you would like data for: Please just enter the year the season finished (e.g., 2021/2022 enter 2022)")

    csv_filename = f"Team{year}.csv"
    
    csv_path = pkg_resources.resource_stream(__name__, f"../{csv_filename}")
        
    TeamData = pd.read_csv(csv_path)
       
    return TeamData


    

def BasicStats():
    df = LoadData()
    team = input("Enter the team name: ")
    stat = input("Enter the stat/column you want (RK, GP, W, L, OT, PTS, PTS/GP, ROW, GF, GA, GD: ")


    team_data = df[df['Team'].str.lower() == team.lower()]

    if team_data.empty:
        print(f"Sorry, the team '{team}' was not found.")
    else:
        if stat not in df.columns:
            print(f"Error: The stat '{stat}' does not exist. Please choose a valid stat.")
        else:
            stat_value = team_data.iloc[0][stat]
            return stat_value

def AdvancedStats():
    df = LoadData()

    team = input("Enter the team name: ")

    team_data = df[df['Team'].str.lower() == team.lower()]

    if team_data.empty:
        print(f"Sorry, the team '{team}' was not found.")
        return
    
    pts_gp = team_data.iloc[0]['PTS'] / team_data.iloc[0]['GP']
    gf_gp = team_data.iloc[0]['GF'] / team_data.iloc[0]['GP'] 
    ga_gp = team_data.iloc[0]['GA'] / team_data.iloc[0]['GP'] 


    result_df = pd.DataFrame({
        'Team': [team],
        'PTS/GP': [pts_gp],
        'GF/GP': [gf_gp],
        'GA/GP': [ga_gp]
    })
    
    return result_df

