def isPalindrome(word):
word = input("Enter the word or number to be checked")
word_list  =  string.split(word)
rev_list = reversed(word)
if(word_list == rev_list):
    print(word + "is a palindrome")
else:
    print(word + "is not a palindrome")
