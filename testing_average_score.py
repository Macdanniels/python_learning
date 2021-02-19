
print("3. Test Average and Grade")

print("Please enter 5 test scores")
 
a = int(input("Score 1: "))
b = int(input("Score 2: "))
c = int(input("Score 3: "))
d = int(input("Score 4: "))
e = int(input("Score 5: "))

def calc_average(w, x, y, z, a):
	return (w + x + y + z + a)//5
	
def determine_grade(x):
	if x >= 90 and x <= 100:
		print("A")
	elif x >= 80 and x <= 89:
		print("B")
	elif x >= 70 and x <= 79:
		print("C")
	elif x >= 60 and x <= 69:
		print("D")	
	elif x < 60:
		print("F")
	
avg = calc_average(a,b,c,d,e)
grade = determine_grade(a) 

print('The Average is: ',avg)

print('\n')
print('| SCORE  | GRADE    |')
print('_____________________')
print('| 90-100 |\tA   |')
print('| 80-89  |\tB   |')
print('| 70-79  |\tC   |')
print('| 60-69  |\tD   |')
print('|  < 60  |\tE   |')
print('_____________________')
