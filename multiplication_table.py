#(speed_converter.py)
# This program converts the speeds 60kph
# through 130 kph (in 10 kph increments)
# to mph.

mult =2

# Print the table headings.
print('MULTIPLICATION         ADDITION \t MULTIPLICATION OF BOTH')
print('-------------------------------------------------------------------')

# Print the speeds.
for y in range(1, 13, 1):
    
    sam =((y*2)*(y+2))
    
    
    
    print(f'2 x {y} = ', y*2, '\t\t', y+2, '\t\t\t',  format((sam), '.2f'))


