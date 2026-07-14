name = "John"
age = 20
language = "Python"
hours = 3

# John is 20 years old.
print(name,"is",age,"years old.")

# Johnis 20 years old. He studies Python 3 hourse a day
print(name,"is",age,"years old. He studies",language,hours,"hours a day.")

# using f-string
print(f"{name} is {age} years old. He studies {language} {hours} hours a day.")



sub1 = 78
sub2 = 87
sub3 = 83

# John scored 248 marks in total
print(f"{name} scored {sub1 + sub2 + sub3} marks in total.")
percent = (sub1 + sub2 + sub3) / 3
print(f"{name} got {round(percent,2)}% .")