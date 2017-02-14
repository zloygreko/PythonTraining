# Дано целое шестизначное число. Необходимо определить, является ли оно счастливым.

print('Type "exit" to quit')
strNum = input('Enter number: ')
while strNum != 'exit':
    if not strNum.isdigit() or len(strNum) % 2 != 0:
        print('Input should be an integer and have even number of digits')
    else:
        halfLength = int(len(strNum) / 2)
        if sum(list(map(int, strNum[:halfLength]))) == sum(list(map(int, strNum[halfLength:]))):
            print('Happy')
        else:
            print('Not happy')
    strNum = input('Enter number: ')
