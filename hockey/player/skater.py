from .player import Player
import pkg_resources

class Skater(Player):
    def __init__(self, year):
        super().__init__(year)
        self.filename = f"skaters{self.year}.csv"
        #csv_path = pkg_resources.resource_stream(__name__, f"../{self.filename}")

    def load_data(self):
        super().load_data(self.filename)

    def basic_stats(self, player_name):
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print(f"\nBasic stats for {player_name.capitalize()} (Year: {self.year})")
            print(f"Name: {player_data['name'].capitalize()}")
            print(f"Team: {player_data['team']}")
            print(f"Position: {player_data['position']}")
            print(f"Goals: {player_data['I_F_goals']}")
            print(f"Points: {player_data['I_F_points']}")
        else:
            print(f"Player {player_name.capitalize()} not found.")

    def advanced_stats(self, player_name):
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print(f"\nAdvanced stats for {player_name.capitalize()} (Year: {self.year})")
            print(f"Name: {player_data['name'].capitalize()}")
            print(f"Team: {player_data['team']}")
            print(f"Position: {player_data['position']}")
            print(f"Corsi Percentage: {player_data['onIce_corsiPercentage']}")
            print(f"Expected Goals: {player_data['I_F_xGoals']}")
            print(f"Fenwick Percentage: {player_data['onIce_fenwickPercentage']}")
        else:
            print(f"Player {player_name.capitalize()} not found.")
