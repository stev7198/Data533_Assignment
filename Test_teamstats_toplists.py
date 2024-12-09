#!/usr/bin/env python
# coding: utf-8

# In[45]:


import unittest
from unittest.mock import patch
import hockey.teamstats.toplists as list

class TestToplists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    def setUp(self): 
        print('Set Up')
        
    def tearDown(self):
        print('Tear Down')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    @patch('hockey.teamstats.toplists.input')
    def test_TopTeams(self, mock_input):
        """Test TopTeams"""

        # Mock the user input for year, number of teams
        mock_input.side_effect = ['2023', 5]

        # Call the TopTeams function
        top_teams = list.TopTeams()

        # Perform assertions
        self.assertIsNotNone(top_teams, "Stat value should not be None")
        self.assertEqual(len(top_teams), 5, "The number of top teams should match the input number")
        self.assertEqual(top_teams.iloc[0]['PTS'], 135, "The team with the highest points should be at the top")
        self.assertEqual(top_teams.iloc[0]['Team'], 'Boston Bruins', "The team with the highest points should be at the top")

    @patch('hockey.teamstats.toplists.input')
    def test_TopAssists(self, mock_input):
        """Test TopAssists"""

        # Mock the user input for year, number of teams
        mock_input.side_effect = ['2024', 6]

        # Call the TopAssists function
        top_players = list.TopAssists()

        # Perform assertions
        self.assertIsNotNone(top_players, "Stat value should not be None")
        self.assertEqual(len(top_players), 6, "The number of top players should match the input number")
        self.assertEqual(top_players.iloc[0]['total_assists'], 100, "The player with the highest assists should be at the top")
        self.assertEqual(top_players.iloc[0]['name'], 'Nikita Kucherov', "The player with the highest assists should be at the top")

    @patch('hockey.teamstats.toplists.input')
    def test_TopGoals(self, mock_input):
        """Test TopGoals"""

        # Mock the user input for year, number of teams
        mock_input.side_effect = ['2021', 3]

        # Call the TopGoals function
        top_players = list.TopGoals()

        # Perform assertions
        self.assertIsNotNone(top_players, "Stat value should not be None")
        self.assertEqual(len(top_players), 3, "The number of top players should match the input number")
        self.assertEqual(top_players.iloc[0]['I_F_goals'], 41, "The player with the highest goals should be at the top")
        self.assertEqual(top_players.iloc[0]['name'], 'Auston Matthews', "The player with the highest assists should be at the top")
        
unittest.main(argv=[''], verbosity=2, exit=False)  


# In[ ]:




