# input() is used to take an input from user

name = input("Enter your name: ")
print(name)

age = input("Enter your age: ")
print(age)

print("My name is",name,"and my age is",age)


num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
result = num1 + num2
print(result) 
# num1 = 10, num2 = 15, result = 1015
# the input stored as a string

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
result = int(num1) + int(num2)
print(result) 
# num1 = 10, num2 = 15, result = 25


year = input("What is the current year? : ")
age = input("What is your age? : ")
born_year = int(year) - int(age)
print("You were born in the year", born_year)