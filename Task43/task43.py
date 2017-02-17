# Дана строка в которой содержатся цифры и буквы. Необходимо расположить все цифры в начале строки, а буквы -- в конце.

import re

print('Type "exit" to quit')
str = input('Input: ')
while str != 'exit':
    result = re.sub('[^0-9]', '', str) + re.sub('[0-9]', '', str)
    print(result)
    str = input('Input: ')
