# Type conversion / Type casting


# Interger --> Float

num1 = 100
print(type(num1)) 

print(num1) # the result is 100
print(float(num1)) # the result is 100.0

num2 = float(num1)

print(type(num1)) # the result is <class 'int'>
print(type(num2)) # the result is <class 'float'>

num1 = float(num1)
print(type(num1)) # the result is <class 'float'>


# Float --> Integer

num3 = 56.45
print(type(num3))

print(num3) # the result is 56.45
print(int(num3)) # the result is 56

print(int(77.85)) # the result is 77 not 78 because it's not rounding off


# Integer, Float --> String

num4 = 1000
s = str(num4)
print(type(s)) # the result is <class 'str'>


# String --> Integer, Float

s1 = '12345'
x = int(s1)
print(type(x)) # the result is <class 'int'>

s2 = '55.34'
y = float(s2)
print(type(y)) # the result is <class 'float'>

# s3 = "Hello"
# print(int(s3))
# this is not possible. You can't convert a string value to integer or float value 

# s4 = "Python3.13"
# print(int(s4))
# this is not possible. You can't convert a string value to integer or float value 


language = "Python" # str
version = 3.13 # float
# print(language + version) 
# this gives an error. can only concatenate str (not "float") to str

print(language + str(version)) 
# the result is Python3.13

print('100' + '100')
# the result is 100100

print(int('100') + int('100'))
# the result is 200



# <-----Type conversion - boolean----->

val1 = True
print(type(val1))

B = str(val1)
print(type(B)) # the result is <class 'int'> --> 'True'

bool('Python') # True
bool(100) # True
bool(-100) # True
bool(1.5) # True
bool(0) # False
bool(0.0) # Flase
bool(0.5) # True
bool(" ") # True --> space is a valid character
bool('') # False --> Empty string => '', "", '''''', """"""
bool(None) #Flase

int(True) # the result is 1
int(False) # the result is 0

float(True) # the result is 1.0
float(False) # the result is 0.0