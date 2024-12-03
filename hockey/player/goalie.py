from .player import Player
import pkg_resources

class Goalie(Player):
    def __init__(self, year):
        super().__init__(year)
        self.filename = f"goalies{self.year}.csv"
        #csv_path = pkg_resources.resource_stream(__name__, f"../{self.filename}")

    def load_data(self):
        super().load_data(self.filename)

    def basic_stats(self, player_name):
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print(f"\nGoalie Basic Stats for {player_name.capitalize()} (Year: {self.year})")
            print(f"Name: {player_data['name'].capitalize()}")
            print(f"Team: {player_data['Team']}")
            print(f"Wins: {player_data['W']}")
            print(f"Games Played: {player_data['GP']}")
            print(f"Save Percentage (SV%): {player_data['SV%']}")
        else:
            print(f"Goalie {player_name.capitalize()} not found.")

    def advanced_stats(self, player_name):
        player_data = self._get_player_data(player_name)
        if player_data is not None:
            print(f"\nGoalie Advanced Stats for {player_name.capitalize()} (Year: {self.year})")
            print(f"Name: {player_data['name'].capitalize()}")
            print(f"Team: {player_data['Team']}")
            print(f"Goals Against Average (GAA): {player_data['GAA']}")
            print(f"Save Percentage (SV%): {player_data['SV%']}")
            print(f"Shutouts: {player_data['SO']}")
            print(f"Total Saves: {player_data['SV']}")
        else:
            print(f"Goalie {player_name.capitalize()} not found.")
