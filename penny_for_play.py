#A  program that calculates penny for play and Accumulates!!!
import array
import math
day= []
total = 0
t =0
amount_per_day = []
    
print("PENNY FOR PAY ")

days = int( input('HOW MANY DAYS ARE YOU LOOKING AT:'))

for i in range(days):
    
    d = int(input(f'ENTER FOR DAY {i+1} : '))
    day.append(d)

    t +=d

print('\n ')
print('SN       DAY      PAY')
for j in range(len(day)):
    
    #total = amount_per_day[j]
    #double = (amount_per_day[j]*1)
    
    print(f"{j+1}\t","Day",j+1 ,"\t", "$",day[j])
print("---------------------") 
#displaying the salary........................

print('Your salary is: $',t)

#daniel's accumulations




 
