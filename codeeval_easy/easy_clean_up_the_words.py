"""Sample code to read in test cases:
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        s = list(test)
        for i, character in enumerate(s):
            char_int = ord(character)
            if char_int < ord('A') or \
                ord('Z') < char_int and char_int < ord('a') or \
                ord('z') < char_int:
                s[i] = ' '
        test = "".join(s).split()
        test = " ".join(test).lower()
        print(test)