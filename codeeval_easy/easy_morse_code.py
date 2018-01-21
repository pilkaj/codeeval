import sys

morse_code = {  '.-'    : 'A',
                '-...'  : 'B',
                '-.-.'  : 'C',
                '-..'   : 'D',
                '.'     : 'E',
                '..-.'  : 'F',
                '--.'   : 'G',
                '....'  : 'H',
                '..'    : 'I',
                '.---'  : 'J',
                '-.-'   : 'K',
                '.-..'  : 'L',
                '--'    : 'M',
                '-.'    : 'N',
                '---'   : 'O',
                '.--.'  : 'P',
                '--.-'  : 'Q',
                '.-.'   : 'R',
                '...'   : 'S',
                '-'     : 'T',
                '..-'   : 'U',
                '...-'  : 'V',
                '.--'   : 'W',
                '-..-'  : 'X',
                '-.--'  : 'Y',
                '--..'  : 'Z',
                '.----' : '1',
                '..---' : '2',
                '...--' : '3',
                '....-' : '4',
                '.....' : '5',
                '-....' : '6',
                '--...' : '7',
                '---..' : '8',
                '----.' : '9',
                '-----' : '0'
                }

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        words = test.split('  ')
        for word in words:
            text = ""
            for letter in word.split():
                text += morse_code[letter]
            print(text, end=' ')
        print()
