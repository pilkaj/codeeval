"""Sample code to read in test cases:
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        dictionary = {  'a' : '0',
                        'b' : 1,
                        'c' : 2,
                        'd' : 3,
                        'e' : 4,
                        'f' : 5,
                        'g' : 6,
                        'h' : 7,
                        'i' : 8,
                        'j' : 9}
        output = ""
        for character in test:
            if character in dictionary:
                output = output + str(dictionary[character])
            elif '0' <= character and character <= '9':
                output = output + character
        if output == "":
            print("NONE")
        else:
            print(output)
