# Data533_Assignment Hockey Package

We will create a database system to manage data from the last five NHL seasons. The main package will contain three types of databases:
1.	Team Statistics: Data on games played, wins, losses, points, etc.
2.	Goalie Statistics: Data on games played, wins, saves, etc.
3.	Skater Statisitics: Data on goals, assists, position, etc.

Additionally, there will be two subpackages:

## Subpackage 1: teamstats
***basic Module:*** Displays the basic stats for the teams given a year from the user
1. LoadData - Loads and return the correct data for the given year
2. BasicStats - Allows the user to retrieve a stat for a specific team and year (RK, GP, W, L, OT, PTS, PTS/GP, ROW, GF, GA, GD)
3. AdvancedStats - Allows the user to retrieve PTS/GP, GF/GP and GA/GP for a specific team and year

***toplists Module:*** Generate lists for the top teams, players with the most assists, and most goals
1. TopTeams - Allows the user to choose an NHL season, and show the teams with the most points from that year
2. TopAssists - Allows the user to choose an NHL season, and show the players with most assists from that year
3. TopGoals - Allows the user to choose an NHL season, and displays the players with the most goals from that year

## Subpackage 2: player
***player Module:*** Allows for the creation of a player class to retrieve player data.
1. load_data - Loads and return the correct data for the given year
2. get_player_data - Loads and return the correct data for the given player within the year
   
***skater Module:*** Allows for the creation of a skater class to retrieve skater data - subclass of player.
1. load_data - Loads and return the correct data for the given year - calls from player parent class
2. basic_stats - Allows the user to retrieve basic stats for a skater in the chosen year (team, position, goals, points)
3. advanced_stats - Allows the user to retrieve advanced stats for a skater in the chosen year (Corsi percentage, Fenwick percentage)
   
***goalie Module:*** Allows for the creation of a skater class to retrieve goalie data - subclass of player.
1. load_data - Loads and return the correct data for the given year - calls from player parent class
2. basic_stats - Allows the user to retrieve basic stats for a goalie in the chosen year (team, wins, games played, save percentage)
3. advanced_stats - Allows the user to retrieve advanced stats for a goalie in the chosen year (goals against average, shutouts, total number of saves)



***TravisCI Badge***
[![Build Status](https://app.travis-ci.com/stev7198/Data533_Assignment.svg?token=2jTmhrmhivmbSbeqqtUe&branch=main)](https://app.travis-ci.com/stev7198/Data533_Assignment)

***PyPi Package Link***
https://pypi.org/project/HockeyPackage/0.0.1/