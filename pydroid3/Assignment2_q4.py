
def main():

    
	word_file = open('philosophers.txt', 'r')
	word_List = []
	for queue in word_file:

		word_List.append(queue)

	word_count(word_List)
	longest_word(word_List)
	average_length(word_List)
		
	word_file.close()

def word_count(list):
	count = 0
	for j in list:
		count += 1
	print("The number of words in the file is : ",count)
	
#calculating longest word	
def longest_word(list):
	max = list[0]
	temp = len(list[0])

	for j in list:
		if len(j) > temp:
			temp = len(j)   #length of each word 
			max = j
	print("The word with the longest length is", max)
	
	
def average_length(list):
	number_of_Words = 0
	total = 0
	for j in list:
		number_of_Words += 1
		total += len(j)
		average = total // number_of_Words
	print("Average number of words is", average)	

main()