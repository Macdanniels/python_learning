#A  program that calculates penny for play and Accumulates!!!
import array
import math
day1=1
day2=1
days= []
total = 0

amount_per_day = []
    
print("PENNY FOR PAY ")
print("TODAYS WAGE WILL BE INCLUDED ")
days = int( input('HOW MANY DAYS HAVE YOU WORKED ASIDE TODAY:'))

for i in range(days):
    day2 = day1 + day1
    day1 = day2
    amount_per_day.append(day1)

print("SN       DAY    WAGE ")
print("---------------------")
print(i+2-days,  "\t "   'Day',i+2-days, "\t",   "$ 1")

for j in range(len(amount_per_day)):
   
      print(f"{j+2}\t","Day",j+2, "\t", "$",amount_per_day[j])
print("---------------------") 
#displaying the salary........................

print('Your salary is: $',(sum(amount_per_day)+1))

