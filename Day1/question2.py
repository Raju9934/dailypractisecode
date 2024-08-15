#Write the code to find the length of a string without using the string functions.
def lengthofstr(string):
    length=0
    for char in string:
        length+=1
    return length

s="Hello"
length=lengthofstr(s)
print("Length of string:",length)


