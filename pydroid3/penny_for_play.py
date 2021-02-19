#A  program that calculates penny for play
import array
import math
day= []
total = 0
amount_per_day = []
    
print("PENNY FOR PAY ")

days = int( input('HOW MANY DAYS ARE YOU LOOKING AT:'))

for i in range(days):
    
    d = int(input(f'ENTER FOR DAY {i+1} : '))
    day.append(d)

    t = amount_per_day.append((i+1)*d)

print('\n ')
print('SN      DAY      PAY')
for j in range(len(amount_per_day)):
    
    total += amount_per_day[j]

    print(f"{j+1}\t",j+1 ,"\t", "$",amount_per_day[j]) 
print("---------------------") 
#displaying the salary........................

print('Your salary is: $',total)




 
