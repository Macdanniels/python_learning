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
for i in range(count):
    while  word == True:
       word =  (input(f'Please Input you Word {i+1}: '))
       if word == 0:
           break
       word_list.append(word)

     #calculating the length of the whole characteristics  
       length = len(word_list[i])

   # average= sum(word_list[i])/len(word_list[i])
print('\nThe average is ',average)
print('\nThe length is ',length)
print('\nThe list is ',word_list)

 

