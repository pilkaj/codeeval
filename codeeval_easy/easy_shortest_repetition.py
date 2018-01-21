"""Sample code to read in test cases:
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        #print(test, end=' ')
        test = test.strip('\n')
        period = 1
        size = len(test)
        while period <= size:
            if size%period == 0:
                pattern = test[0:period]*int(size/period)
                if pattern == test:
                    print(period)
                    break
            period += 1
