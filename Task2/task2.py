# Дано положительное целое число. Необходимо проверить, образуют ли цифры этого числа возрастающую последовательность.

print('Type "exit" to quit')
strNum = input('Enter number: ')
while strNum != 'exit':
    if not strNum.isdigit():
        print('Input should be positive integer')
    else:
        if len(strNum) > 1:
            for x, y in zip(strNum, strNum[1:]):
                if y <= x:
                    print('Not ascending')
                    break
            else:
                print('Ascending')
        else:
            print('Not ascending')
    strNum = input('Enter number: ')
