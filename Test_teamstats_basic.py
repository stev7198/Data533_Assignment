#!/usr/bin/env python
# coding: utf-8

# In[24]:


import unittest
from unittest.mock import patch
import hockey.teamstats.basic as basic

class TestBasic(unittest.TestCase):
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

    @patch('hockey.teamstats.basic.input')
    def test_BasicStats(self, mock_input):
        """Test BasicStats"""

        # Mock the user input for year, team, and stat
        mock_input.side_effect = ['2022', 'Seattle Kraken', 'W']

        # Call the BasicStats function
        stat_value = basic.BasicStats()

        # Perform assertions
        self.assertIsNotNone(stat_value, "Stat value should not be None")
        self.assertEqual(stat_value, 27, "The W stat for TeamA should be 27")

    @patch('hockey.teamstats.basic.input')
    def test_AdvancedStats(self, mock_input):
        """Test AdvancedStats"""

        # Mock the user input for year, team
        mock_input.side_effect = ['2022', 'Montreal Canadiens']

        # Call the AdvancedStats function
        stat_df = basic.AdvancedStats()

        # Perform assertions
        self.assertIsNotNone(stat_df, "Stat value should not be None")
        self.assertTrue('Montreal Canadiens' in stat_df['Team'].values, "Team should be Montreal Canadiens")
        self.assertAlmostEqual(stat_df['PTS/GP'].iloc[0], 0.6707, places=4,
                               msg="PTS/GP should be correctly calculated")
        self.assertAlmostEqual(stat_df['GF/GP'].iloc[0], 2.6951, places=4,
                               msg="GF/GP should be correctly calculated")
        self.assertAlmostEqual(stat_df['GA/GP'].iloc[0], 3.8902, places=4,
                               msg="GA/GP should be correctly calculated")
        
unittest.main(argv=[''], verbosity=2, exit=False)  


# In[ ]:




