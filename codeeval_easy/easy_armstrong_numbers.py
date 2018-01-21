"""Sample code to read in test cases:
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        number = test.strip('\n')
        power = len(number)
        #print(number)
        #print(power)
        sum = 0
        for digit in number:
            #print(" digit:{0}".format(digit))
            sum += int(digit)**power
            #print(" sum = {0}".format(sum))
        if int(number) == sum:
            print("True")
        else:
            print("False")
