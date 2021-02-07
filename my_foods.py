my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(friend_foods)
print(my_foods)
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(friend_foods)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 250)
print("\ndimensions modified:")
for dimension in dimensions:
	print(dimension)
	





