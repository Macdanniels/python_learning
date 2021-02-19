#prime number checks

print("A program that check for Prime Number!!")
num1 = int(input("Enter a number: "))  

if num1 == 0:
     print("you entered 0 which is an exception!!!")

     
if num1 > 1:  
   for i in range(2, num1//2):  
       if(num1% i) == 0:
         print(bool( ))  
         print(num1,"is not a prime number!!!")
                   
         #   print(i,"times",num1//i,"is",num1)
         break
    else:
         print(bool())  
         print(num1,"is a prime number")
         
else:
  print(num1,"is not a prime number!")


 

   
   