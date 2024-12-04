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
