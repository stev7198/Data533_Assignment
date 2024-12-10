import unittest

from Test_teamstats_basic import TestBasic
from Test_teamstats_toplists import TestToplists

#testing for the Teamstats subpackage 

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestBasic('test_BasicStats'))
    suite.addTest(TestBasic('test_AdvancedStats'))
    suite.addTest(TestToplists('test_TopTeams'))
    suite.addTest(TestToplists('test_TopAssists'))
    suite.addTest(TestToplists('test_TopGoals'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()

from test_get_player_stats import TestGetUserInput
from test_player import TestPlayer 
from test_skater import TestSkater
from test_goalie import TestGoalie

#testing for the player subpackage

def player_suite():
    suite = unittest.TestSuite()
    
    # Add each test case method from the TestGetUserInput class to the suite
    suite.addTest(TestGetUserInput('test_get_player_stats_skater'))
    suite.addTest(TestGetUserInput('test_get_player_stats_goalie'))
    suite.addTest(TestGetUserInput('test_get_player_stats_invalid_player_type'))

    # Add each test case method from the TestPlayer class to the suite 
    suite.addTest(TestPlayer('test_initialization'))
    suite.addTest(TestPlayer('test_load_data_file_not_found'))
    suite.addTest(TestPlayer('test_get_player_data_found'))
    suite.addTest(TestPlayer('test_get_player_data_not_found'))

    # Add each test case method from the TestSkater class to the suite
    suite.addTest(TestSkater('test_initialization'))
    suite.addTest(TestSkater('test_load_data_file_not_found'))
    suite.addTest(TestSkater('test_basic_stats_found'))
    suite.addTest(TestSkater('test_basic_stats_not_found'))
    suite.addTest(TestSkater('test_advanced_stats_found'))
    suite.addTest(TestSkater('test_advanced_stats_not_found'))

    # Add each test case method from the TestGoalieclass to the suite
    suite.addTest(TestGoalie('test_initialization'))
    suite.addTest(TestGoalie('test_load_data_file_not_found'))
    suite.addTest(TestGoalie('test_basic_stats_found'))
    suite.addTest(TestGoalie('test_basic_stats_not_found'))
    suite.addTest(TestGoalie('test_advanced_stats_found'))
    suite.addTest(TestGoalie('test_advanced_stats_not_found'))
    
    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity=2 gives more detailed output
    result = runner.run(suite)

# Run the suite
if __name__ == '__main__':
    player_suite()
