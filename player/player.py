import pandas as pd

#Alter to include seasons starting 2010-2014.

# Base class for both Skater and Goalie
class Player:
    def __init__(self, year):
        self.year = year
        self.data = None

    def load_data(self, filename):
        try:
            # Load the data for both skaters and goalies (different filenames)
            self.data = pd.read_csv(filename, encoding='ISO-8859-1')
        except FileNotFoundError:
            print(f"Error: The file for the year {self.year} was not found.")
        except UnicodeDecodeError:
            print(f"Error: There was a problem decoding the file {filename}. Please check the file's encoding.")

    def display_stats(self, player_name):
        if self.data is None:
            return
        
        # Normalize player names to lowercase for case-insensitive comparison
        self.data['name'] = self.data['name'].str.lower()

        if player_name in self.data['name'].values:
            player_data = self.data[self.data['name'] == player_name].iloc[0]
            return player_data
        else:
            return None
