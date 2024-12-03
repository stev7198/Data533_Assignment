import pandas as pd
import pkg_resources

class Player:
    def __init__(self, year):
        self.year = year
        self.data = None

    def load_data(self, filename):
        
        try:
            csv_path = pkg_resources.resource_stream(__name__, f"../{self.filename}")
            self.data = pd.read_csv(csv_path, encoding='ISO-8859-1')
        except FileNotFoundError:
            print(f"Error: The file for the year {self.year} was not found.")
        except UnicodeDecodeError:
            print(f"Error: There was a problem decoding the file {filename}. Please check the file's encoding.")
 
    def _get_player_data(self, player_name):
        """Helper function to filter player data"""
        if self.data is None:
            return None
        
       
        self.data['name'] = self.data['name'].str.lower()
        
        
        if 'situation' in self.data.columns:
            player_data = self.data[(self.data['name'] == player_name) & (self.data['situation'] == 'all')]
        else:
            player_data = self.data[self.data['name'] == player_name]
        
        
        if not player_data.empty:
            return player_data.iloc[0]  
        return Nonee
