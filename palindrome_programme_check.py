
#palindrome programme
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length -1
    status = 1
    while(first<last):
           if(string[first] == string[last]):
               first = first + 1
               last = last - 1
           else:
              status = 0
              break
    return int(status)
string = input('Enter the String:  ')
status = check_palindrome(string)
if(status):
     print('This is a palindrome ')
else:
     print('This is not a palindrome ')
