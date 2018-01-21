"""Sample code to read in test cases:
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        test = test.strip('\n')
        players, number = test.split('|')
        players = players.split()
        number = int(number)
        
        size = len(players)
        while size > 1:
            players.pop((number%size) - 1)
            size = len(players)
        print(players[0])
        