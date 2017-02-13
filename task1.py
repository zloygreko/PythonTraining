
print('Type "exit" to quit')
strNum = input("Enter number: ")
while strNum != 'exit':
    if (not strNum.isdigit()) or (len(strNum) != 6):
        print('Input should be an integer and have 6 digits')
    else:
        if sum(list(map(int, strNum[0:3]))) == sum(list(map(int, strNum[3:6]))):
            print('Happy')
        else:
            print('Not happy')
    strNum = input("Enter number: ")
