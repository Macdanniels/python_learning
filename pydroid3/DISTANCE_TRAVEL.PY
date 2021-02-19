#A  program that calculates calrories as it is being burn
import array
speed= []
time = []
result = []
    
print("DISTANCE TRAVELED ")

Journey = int( input('how many tour did you make:'))

for i in range(Journey):
    
    spd = int(input(f'ENTER SPEED {i+1} COVERED IN MILES/HOUR: '))
    speed.append(spd)
    t= int(input(f'ENTER THE HOURS COVERED WITH THIS SPEED {i+1}: '))
    time.append(t)
    result.append(t*spd)

print('\n ')
print('SN      HOUR       DISTANCE TRAVELED')

for j in range(len(result)):
 
    print(f"{j+1}\t", time[j]  ,"\t\t", result[j]) 

    #print(f"{i+1}\t",i ,"\t\t", result)  
  #  print(dist)    




 
