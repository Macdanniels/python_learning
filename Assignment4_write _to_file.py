# This program writes three lines of data
# to a file.



def main():
    
# Open a file named philosophers.txt.
    
    outputfile = open('word_files.txt', 'w')
    
    count = int(input('how many words do you want to type: '))
    
     
       
def  write_file():
      
      count = main()
      
      for i in range (count):  
       # Writing the words!!!
       # to the file.
       # print(f'Kindly enter word {i} : ')
        outputfile.write(' \n')    

        # Close the file.
        outputfile.close()

# Call the main function.
main()