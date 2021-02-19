
ocean_deep =1.6
trials =[ ]
readings =25
click =['YES']
while True:
    click = str(input("Are sure you want to run this for 25 years, Yes/No: ")).upper()
    trials.append(click)
    if click != 'YES':
        print('Opps!!! Sorry') 

    break
if click == 'YES':
    print('SN       YEAR\t READINGS')    
    for i in range (readings):
     year = 2021
     print(f'{i+1}\t', year+(i+1),' \t', int((i+1)*ocean_deep) ,'mm')
