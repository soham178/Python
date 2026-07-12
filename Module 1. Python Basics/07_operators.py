# x = 10
# y = x + 20

# x, y --> Variables
# 20 --> Value/literal
# =, + --> Operators

# operator => Operators are symbols to perform certain operations. An operations contains two things Operators(=, +) and Operands (x,y,20)



# <-----Arithmetic Operators----->

num1 = 10
num2 = 5

# + --> Addition
print(num1 + num2) # 15

# - => Substarction
print(num1 - num2) # 5

# * => Multiplication
print(num1 * num2) # 50

# / => Division
print(num1 / num2) # 2.0 --> the / operator gives the result in floating number

# // => Floor Division
print(num1 // num2) # 2
print(10 // 3) # 3

# % => Modulus
print(10 % 3) # 1 --> gives the reminder
print(num1 % num2) # 0

# ** => Exponent
print(5 ** 2) # 25 --> 5 * 5
print(3 ** 4) # 81 --> 3 * 3 * 3 * 3



# <-----Assigment Operators----->

value = 100 # here '=' is an assigment operator

# '+=' assigment operator
x = 10
x += 1 # x = x + 1
print(x) # 11

# '-=' assigment operator
x -= 6 # x = x - 6
print(x) # 5

# '*=' assigment operator
x *= 10 # x = x * 10
print(x) # 50

# '/=' assigment operator
x /= 20 # x = x / 20
print(x) # 2.5



# <-----Comparison Operators----->

# == --> double equal
num1 = 100
num2 = 90
num3 = 90
print(num2 == num3) # the result is True
print(num1 == num2) # the result is False
print('Python' == 'python') # the result is False
print('python' == 'python') # the result is True
print(100 == '100') # the result is False

# != --> not equal
print(num2 != num3) # the result is False
print(num1 != num2) # the result is True
print('Python' != 'python') # the result is True
print('python' != 'python') # the result is False
print(100 != '100') # the result is True

# > --> greater than
print(num1 > num2) # True
print(num3 > num1) # False
print(num2 > num3) # False

# < --> less than
print(num1 < num2) # False
print(num3 < num1) # True
print(num2 < num3) # False

# >= --> greater than equal
print(num1 >= num2) # True
print(num3 >= num1) # False
print(num2 >= num3) # True

# <= --> less than equal
print(num1 <= num2) # False
print(num3 <= num1) # True
print(num2 <= num3) # True



# <-----Logical Operators----->

# and
True and True # True
True and False # False
False and True # False
False and False # False

# or
True or True # True
True or False # True
False or True # True
False or False # False

# not
not True # False
not False # True


name = "Mark"
age = 25

name == "Mark" and age >=18 # True
name == "Mark" and age == 30 # False
name == "Mark" or age == 30 # True



# <-----Associativity & Precedence of operators----->

5 + 10 * 6 # 65
(5 + 10) * 6 # 90

name == "Mark" or name == "John" and age < 18 # True
(name == "Mark" or name == "John") and age < 18 # False

100 / 10 * 10 # 100.0 --> left to right
100 / (10 * 10) # 1.0

2 ** 1 ** 3 # 2 --> Right to left



# <-----Classification of operators based on the number of operands----->

# Unary --> 1 operand
-10
not True

# Binary --> 2 operands
10 - 5
True or False

# Ternary --> 3 Operands