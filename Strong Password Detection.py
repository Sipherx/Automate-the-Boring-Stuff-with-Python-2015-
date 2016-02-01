import re

def password(userinput):
    passRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\w]{8,}$')
    result = passRegex.search(userinput) 
    return result 
        

while True:
    print('Please enter a strong password')
    print('\t(at least 8 characters long, \n\t upper and lower case,\
          \n\t with at least 1 digit)')

    user = input('Password: ')
    if password(user) != None:
        print('Your password is: ', password(user).group())
        break
   
        

