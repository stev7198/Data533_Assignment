class Goalie(Player):
    def __init__(self, year):
        super().__init__(year)
        self.filename = f"goalies{self.year}.csv"

    def load_data(self):
        super().load_data(self.filename)

    def _get_player_data(self, player_name):
        """ Helper function to filter player data """
        data_filtered = self.data[self.data['situation'] == 'all']
        if player_name in data_filtered['name'].values:
            return data_filtered[data_filtered['name'] == player_name].iloc[0]
        return None

    def display_stats(self, player_name):
        """ Display goalie stats """
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
            print("Goalie not found. Please check the spelling and try again.")

    def _show_basic_stats(self, player_name):
        """ Show basic stats for the goalie """
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print("\nGoalie stats for the year", self.year)
            print(f"Name: {str(player_data['name']).capitalize()}")
            print(f"Team: {player_data['Team']}")
            print(f"Wins: {player_data['W']}")
            print(f"Games Played: {player_data['GP']}")
            print(f"Save Percentage (SV%): {player_data['SV%']}")
        else:
            print("Goalie not found. Please check the spelling and try again.")

    def _show_advanced_stats(self, player_name):
        """ Show advanced stats for the goalie """
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print("\nAdvanced goalie stats for the year", self.year)
            print(f"Name: {str(player_data['name']).capitalize()}")
            print(f"Team: {player_data['team']}")
            print(f"Goals Against Average (GAA): {player_data['GAA']}")
            print(f"Save Percentage (SV%): {player_data['SV%']}")
            print(f"Shutouts: {player_data['SO']}")
            print(f"Total Saves: {player_data['SV']}")
        else:
            print("Goalie not found. Please check the spelling and try again.")
