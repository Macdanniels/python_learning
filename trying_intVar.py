#slicing in python

str ="excellent score"
s1 = slice(4)  # print first four value

s2 = slice(2,7,11,) #printing the start, stop stop steps on indexing

print(str[s1])
print(str[s2])
print("+++++++++++++++++++++++++++++++++++++")


#removing character from an indexing 

def value(str):  #where str is a parameter
    result = ""
    for a in range (len(str)):
        if a %2 == 0:
            result = result + str[a]
        return result
print(value('string'))
print(value('Prototype'))
