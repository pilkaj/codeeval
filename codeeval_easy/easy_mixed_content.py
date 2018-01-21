import sys

with open(sys.argv[1], 'r') as test_case:
    for test in test_case:
        test = test.strip('\n')
        numbers = []
        words = []
        test = test.split(',')
        for each in test:
            if '0' <= (each[0]) and (each[0]) <= '9':
                numbers.append(each)
            else:
                words.append(each)
        print(",".join(words), end='')
        if not words == [] and not numbers == []:
            print("|", end='')
        print(",".join(numbers))
