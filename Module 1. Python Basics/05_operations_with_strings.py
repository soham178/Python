s1 = "Hello World"
print(s1)
print(type(s1))

s2 = "We are learning Python"
print(s2)
print(type(s2))

s3 = """Hello everyone.
We are looking at strings.
Bye"""
print(s3)
print(type(s3))


# How to find the length of the string? --> length of a string means how many characters are there in a string 

s4 = "Python" # there are 6 characters
print(len(s4)) # the result is 6
print(len(s1)) # the result is 11 --> space is also a character in python so the result is not 10 but 11


# What is indexing? --> every character have a internal position

# Python --> 012345 --> indexing starts with 0
# Python --> -6 -5 -4 -3 -2 -1 --> negative indexing

print(s4[0]) # the result is P
print(s4[1]) # the result is y
print(s4[2]) # the result is t
print(s4[3]) # the result is h
print(s4[4]) # the result is o
print(s4[5]) # the result is n
# print(s4[6]) # the result is error
print(s4[-6]) # the result is P
print(s4[-5]) # the result is y
print(s4[-4]) # the result is t
print(s4[-3]) # the result is h
print(s4[-2]) # the result is o
print(s4[-1]) # the result is n


# How to join string together? --> concatenation of strings

print(s1 + s2)
# the result is Hello WorldWe are learning Python

print(s1 + ' ' + s2)
# the result is Hello World We are learning Python