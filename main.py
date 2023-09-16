a = input('''
Write your sentence here.
>> ''')
print()
for i in a:
  if i == 'r' or i == 'R':
    print('\033[1;31m', end='')
    print(i, end='')
  elif i == 'y' or i == 'Y':
    print('\033[1;33m', end='')
    print(i, end='')
  elif i == 'b' or i == 'B':
    print('\033[34m', end='')
    print(i, end='')
  elif i == 'g' or i == 'G':
    print('\033[32m', end='')
    print(i, end='')
  elif i == 'p' or i == 'P':
    print('\033[1;35m', end='')
    print(i, end='')
  elif i == ' ':
    print('\033[0m', end='')
    print(i, end='')
  else:
    print(i, end='')
    