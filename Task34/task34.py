# Дана строка в которой числа перечислены через пробел. Необходимо найти максимальное из этих чисел.

import re

print('Type "exit" to quit')
str = input('Input: ')
while str != 'exit':
    print(max(list(map(int, re.sub('\s+', '', str)))))
    str = input('Input: ')