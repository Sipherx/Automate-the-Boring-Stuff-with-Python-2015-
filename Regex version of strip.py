import re

def stripper(string, char=' '):
    stringRegex = re.compile(char, re.I)
    convert = stringRegex.sub('', string)
    print(convert)

    
message = input('Enter a string \n')
c = input('Enter the character that you want to remove!\nIf nothing\
 is entered, space will be removed\n')

if c != '':
    stripper(message, c)
else:
    stripper(message)
