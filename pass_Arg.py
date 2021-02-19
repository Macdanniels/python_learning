# This program demonstrates an argument being
# passed to a function.

def main():
    value =int(input('Enter a value: '))
    show_double(value)

# The show_double function accepts an argument
# and displays double its value.
def show_double(number):
    result = number * 2
    print(result)

 # Call the main function.
main()