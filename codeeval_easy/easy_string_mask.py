import sys

diff = ord('a') - ord('A')

with open(sys.argv[1], 'r') as test_case:
    for test in test_case:
        test = test.strip('\n')
        word, code = test.split()
        result = ""
        for i in range(len(code)):
            letter = word[i]
            if code[i] == '1':
                letter = chr(ord(letter) - diff)
            result += letter
        print(result)