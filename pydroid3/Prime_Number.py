
# Program to check if a number is prime or not

# To take input from the use
#
def main():

    print("================================================")
    print("HERE LIES THE PRIME NUMBERS BETWEEN 900 AND 1000")
    print("================================================")

    num = int(input("Enter a number: "))
    
    
    # prime numbers are greater than 1
    if num > 1:
    # check for factors
        for i in range(2,num//2):
            if (num % i) == 0:
                return False
        print(num,"is not a prime number")
        #    print(i,"times",num//i,"is",num)
        
    else:
        print("True")
        print(num,"is a prime number")
        
    # if input number is less than
    # or equal to 1, it is not prime
    print("HERE LIES THE PRIME NUMBERS BETWEEN 900 AND 1000")
    is_prime(num)
        

def is_prime(j):
    
    for j in range (900,1000 ):
        if( j > 1):
         for i in (2,j):
            if(j%i) == 0:
                
                break
            
            else:
                
                print(j)

main()
