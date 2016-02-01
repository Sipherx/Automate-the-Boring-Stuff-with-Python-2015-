#! python 3.5
# regex search.py - opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression

import os, re
def search(regex, txt):
    searchRegex = re.compile(regex, re.I)
    result = searchRegex.findall(txt)
    print(result)
    
while True:
    dirs = input('Enter the absolute path of the folder that you want to search\n')
    if os.path.exists(dirs) == True:
        print('This folder exists')
        break
user_search = input('Enter the regular expression\n')


folder = os.listdir(dirs)

for file in folder:
    if file.endswith('.txt'):
        print(os.path.join(dirs, file))
        txtfile = open(os.path.join(dirs, file), 'r+')
        msg = txtfile.read()
        search(user_search, msg)
       
        
        

