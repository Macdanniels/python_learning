#A  program that calculates calrories as it is being burn


list = [10, 15, 20, 25, 30]
q = "yes"
calorie = 4.2
print("A program that calculates CALORIES BURN")
q =  input('Do you want to run this program yes/No: ')
if q == "yes":

    for minute in range(10, 35, 5):
        result = calorie * minute
        
        print(result,f'calories burn in {minute} minutes')
    
else:
    print('Thank you')
    


 
