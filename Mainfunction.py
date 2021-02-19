#A function program

def main():
    nums = input('Enter some numbers seperated by spaces: ')
    num_list =[]
    for i in nums.split(" "):
        num_list.append(int(i))
    print("Passing to addition function")
    print("The sum of all the numbers is: ", addition(num_list))

    print("Passing to Multiplication function")
    print("The product of all the numbers is: ", product(num_list))


    print("Passing to Average function")
    print("The Average of all the numbers is: ",average(num_list))

def addition(a_list):
    total =0
    for i in a_list:
        total +=i
    return total

def product(a_list):
    total =1
    for i in a_list:
        total *=i
    return total


def average(a_list):
    avg = addition(a_list)/len(a_list)
    return avg

main()



