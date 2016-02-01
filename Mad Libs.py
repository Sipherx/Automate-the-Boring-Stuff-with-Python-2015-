#! python 3.5
# Mad Libs.py - replace adjective, adverb, noun, verb with user desired words

import os, re



modFile = open('C:\\Users\\Kevin\\Desktop\\hi.txt', 'r+')
modWords = modFile.read()

print(modWords)
print('Refill the above sentence'.center(70, '*')+'\n')

wordRegex = re.compile(r'(adjective|adverb|noun|verb)+', re.I)
result = wordRegex.findall(str(modWords))

for i in result:
    
    mod = input('Enter a %s :\n' %i.lower())
    modWords = wordRegex.sub(mod, str(modWords), 1)
    
modFile.seek(0)
modFile.write(modWords)
modFile.truncate()
modFile.close()


