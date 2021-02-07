 # This program demonstrates how a floating-point
# number can be displayed as currency.
monthly_pay = 10000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', 
format(annual_pay, ',.2f'), 
sep='')
#Specifying a Minimum Field Width with comma
print('The number is', format(12345.6789, '12,.3f'))

#Specifying a Minimum Field Width without comma
print('The number is', format(12345.6789, '12.2f'))

# This program displays the following
# floating-point numbers in a column
# with their decimal points aligned.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Display each number in a field of 7 spaces
# with 2 decimal places.
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.1f'))

#formatting a Floating-Point Number as a Percentage

print(format(0.5, '%'))

#Formatting Integers

print(format(12345634, 'd'))
print(format(123456, '10,d'))

#printing to newline

print('Enter the amount of ' + 
'sales for each day and ' + 
'press Enter.')
