"""Sample code to read in test cases:
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        writer = ""
        test = test.strip('\n')
        data, codes = test.split('|')
        codes = codes.split()
        for id in codes:
            writer += data[int(id)-1]
        print(writer)
