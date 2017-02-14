# Дано натуральное число меньшее 512. Необходимо проверить, является ли оно счастливым в двоичном представлении.

strNum = input('Enter number: ')
while True:
    strBin = bin(int(strNum))[2:]
    if len(strBin) % 2 != 0:
        print('Not an even number of digits in binary view')
    else:
        halfLength = int(len(strBin) / 2)
        if sum(list(map(int, strBin[:halfLength]))) == sum(list(map(int, strBin[halfLength:]))):
            print('Happy in binary')
        else:
            print('Not happy in binary')
    strNum = input('Enter number: ')