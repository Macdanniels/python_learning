

print ("You've entered a wording system!")
print ("What words do you want?")

repeat = "y"
while repeat == "y":
    word1 = input ('enter first word:')
    word2 = input( 'enter second word:')

    print (word1)
    print (word2)

    if len(word1)>len(word2):
        word_difference = len(word1) - len(word2)
        print (word1, "is", word_difference, "letters longer than", word2)

    elif len(word2)>len(word1):
        word_difference = len(word2) - len(word1)
        print (word2, "is", word_difference, "letters longer than", word1)

    elif len(word1) == len(word2):
        print (word1, "has same number of letters as", word2)    

    repeat = input("Would you like to enter two more words?(y/n)")