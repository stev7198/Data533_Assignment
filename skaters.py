import pandas as pd
from .player import Player

class Skater(Player):
    def __init__(self, year):
        super().__init__(year)
        self.filename = f"skaters{self.year}.csv"

    def load_data(self):
        super().load_data(self.filename)

    def _get_player_data(self, player_name):
        """ Helper function to filter player data """
        data_filtered = self.data[self.data['situation'] == 'all']
        if player_name in data_filtered['name'].values:
            return data_filtered[data_filtered['name'] == player_name].iloc[0]
        return None

    def display_stats(self, player_name):
        """ Display basic or advanced stats based on user input """
        player_data = super().display_stats(player_name)
        
        if player_data is not None:
            # Ask the user to choose between basic or advanced stats
            stat_type = input("Would you like to see basic stats or advanced stats? (basic/advanced): ").strip().lower()

            if stat_type == 'basic':
                self._show_basic_stats(player_name)

            elif stat_type == 'advanced':
                self._show_advanced_stats(player_name)

            else:
                print("Invalid choice. Please choose either 'basic' or 'advanced'.")
        else:
            print("Player not found. Please check the spelling and try again.")

    def _show_basic_stats(self, player_name):
        """ Show basic stats for the player """
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print("\nPlayer stats for the year", self.year)
            print(f"Name: {str(player_data['name']).capitalize()}")
            print(f"Team: {player_data['team']}")
            print(f"Position: {player_data['position']}")
            print(f"Goals: {player_data['I_F_goals']}")
            print(f"Points: {player_data['I_F_points']}")
        else:
            print("Player not found or no 'all' data for this player. Please check the spelling and try again.")

    def _show_advanced_stats(self, player_name):
        """ Show advanced stats for the player """
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print("\nAdvanced player stats for the year", self.year)
            print(f"Name: {str(player_data['name']).capitalize()}")
            print(f"Team: {player_data['team']}")
            print(f"Position: {player_data['position']}")
            print(f"Corsi Percentage: {player_data['onIce_corsiPercentage']}")
            print(f"Expected Goals: {player_data['I_F_xGoals']}")
            print(f"Fenwick Percentage: {player_data['onIce_fenwickPercentage']}")
        else:
            print("Player not found. Please check the spelling and try again.")
