def commacode(convert):
      newlist = ''
      for i in range(len(convert[:-1])):
            newlist += convert[i] + ', '
      print(newlist + 'and ' + convert[-1])
            



spam = ['apples', 'bananas', 'tofu', 'cats']
commacode(spam)

