#Example,factorial:

n = int(input('How many numbers do you want to check: '))

for j in range(n):
    
    x = int(input('enter the numbers you want to calculates its factorials: '))


if  x>1:

     
     fact = x*X-1

     
     print(f'factorial of {x} is: ',fact)

elif x==1:
     print(f'factorial of 1 is: 1')


    #check if number is negative
elif x<0:
       print('Sorry!, factorial does not exist')

elif x==0:
    print('factorial of 0 is 1')

