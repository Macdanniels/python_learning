#guessing game:

import random


minNumber=1
MaxNumber=51

test = "y"

while test == "y": 
    
     val =int(input('Kindly enter a number you want to guess between 1 and 50: '))
     
         
     for i in range (1):
            rnd = (random.randint(minNumber, MaxNumber))
            print ('The Random number generated is: ', rnd)   

     if(val == rnd):

                print('You are correct:')
                            
     elif (val > MaxNumber ):
        
        print ("Error") 

     elif (val > rnd ):
        print (val, 'higher than',rnd)
        print('Too High')


     elif (val < rnd ):
        
        
        print (val, 'less than',rnd)
        print('Too low')
     
     
     
     else:
        print('Out of loop, Try again:')

     test = input("Would you like to enter two more words?(y/n)")