# This program gets an item's original price and
# calculates its sale price, with a 20% discount.
#in Table 2-3 that Python has two different division operators. The /operator performs floating-point division, and the //operator performs integer division. Both operators 
#divide one number by another. The difference between them is that the /operator gives 
#the result as a floating-point value, and the //operator gives the result as a whole number. 
#Let’s use the interactive mode interpreter to demonstrate:
#5 / 2 Enter
#In this session, we used the /operator to divide 5 by 2. As expected, the result is 2.5. Now 
#let’s use the //operator to perform integer division:
#5 // 2 Enter 2
# As you can see, the result is 2. The //operator works like this:
# When	the	result	is	positive,	it	is	truncated, which means that its fractional part is 
#thrown away.
#When	the	result	is	negative,	it	is	rounded	away from zeroto the nearest integer.
#The following interactive session demonstrates how the //operator works when the result 
#is negative:
#−5 // 2 Enter−3
# Get the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * 0.2
# Calculate the sale price.
sale_price = original_price-discount 
# Display the sale price.
print('The sale price is', sale_price)