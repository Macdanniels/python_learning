#A  program that calculates calrories as it is being burn
import array

avg = []
word_list = []
average = 0
total_words= 0
count_word = 0
length = 0

print("AVERAGE WORDS CHECKER")
count =  int(input('how many words do you want to enter:'))
while  True:   
    word =  (input(f'Please Input you Word: '))
    word_list.append(word)
    if len(word) == 0:
          break
     #calculating the length of the whole characteristics  
    length = [len(i)   for i in word_list]
    average= int(sum(length)/len(word_list))
print("AVERAGE WORDS CHECKER RESULT")
print("_____________________________")
print('\nThe average is ',average)
print('\nThe list is ',word_list)




#Another method here when user didnt enter any word, the App stops and calulates

#DECLARING AN ARRAY
#words = []
#while true:
  #word = str(input("Please enter a word: "))
  #if len(word) == 0:
  #break
#words.append(word)
#numbers_of_characters =len(i)
#numbers_of_characters =[len(i) for i in words]
#average = int(sum(numbers_of_characters/len(words)))





 

