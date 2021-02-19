#Determine grade by students

def main():

    grade = int(input('Enter grade of the student: '))
    print("your score is :", grade)
    
    determine_grade(grade)

#grade entry check


def determine_grade(test_score):
    
    
    if (test_score >= 90) and (test_score <= 100):

          print('A')
                                
    elif (test_score >= 80) and (test_score <= 89):
        
        print ("B") 

    elif (test_score >= 70) and (test_score <= 79):

        print('C')

    elif (test_score >= 60) and (test_score <= 69):

        print('D')

    elif (test_score < 60):

        print('F')


main()