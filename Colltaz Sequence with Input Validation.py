def colltaz(num):
      if num % 2 == 0:
            num //= 2
            print(num, end = ', ')
            return num
      elif num % 2 == 1:
            num = num * 3 + 1
            print(num, end = ', ')
            return num

try:
      usernum = int(input('Please enter an integer \n'))
except ValueError:
      print('You must enter an integer')
y = colltaz(usernum)

while y != 1:
      y = colltaz(y)
