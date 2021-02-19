#factorial:


fact =int(input('Enter the number: '))

value = 1


#checking if enry is negative number
if fact < 0 :
    print('I am Sorry, You entered a negative number:')


elif (fact == 0 ):
     print('factorial of 0 is 1:')

else:
    for i in range(1,fact +1):
        value = value *i
    print('the factorial of ',fact, 'is ', value)


