"""Sample code to read in test cases:
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		print(test)
		decimal = int(test.strip())
		
		while decimal > 0:
			print(decimal%2)
			decimal /= 2
