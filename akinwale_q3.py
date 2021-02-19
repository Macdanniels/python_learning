import math

number_of_test = 5
test_score = 0
total_score = 0.0
def main():
	
	for i in range(1, 6):
	
		 test_score = int(input(f'Enter your score {i}: ') )
		 test_score += i

	calc_average()
	determine_grade( )

def determine_grade(test_score ): 	 
		 

		 if(test_score >= 90) and (test_score <= 100):
			 
			 print("A")
		 elif (test_score >= 80) and  (test_score <= 89):
			 print("B")
		 elif (test_score >= 70  and  test_score <= 79):
			 print("C")
		 elif(test_score >= 60 and test_score <= 69):
			 print("D")
		 elif (test_score < 60):
			 print("F")

		#determine_grade(test_score)
def calc_average():

	average_score = total_score/number_of_test

	print("score "," ", "grade")
	print("---------------------")
	print(calc_average(), " ", determine_grade())


main() 