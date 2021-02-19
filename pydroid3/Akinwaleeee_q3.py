#aking how many player names would be included

def main():
   names= int(input("How many player's record are you putting in theis file?: "))
   #open the file
   glf_file = open("golf.txt", "w")

   #getting the players data
   for values in range (1, names + 1):
      #getting the name of player
      print("Enter data for the players #", values,  sep="")
      name = input("Name: ")
      golf_scores = input("Golf_Scores: ")

      glf_file.write(name + "\n")
      glf_file.write(golf_scores + "\n")

      print()

   glf_file.close()
   print("Data is saved in golf.txt file")



def display():
    glf_file= open("golf.txt", "r")
    name = glf_file.readline()

    while name !="":
        golf_scores = glf_file.readline()
        name = name.rstrip("\n")
        golf_scores = golf_scores.rstrip("\n")

        print("Name:", name)
        print("Golf scores: ", golf_scores)
        print()

        name = glf_file.readline()
        
        glf_file.close()
        display()

main()