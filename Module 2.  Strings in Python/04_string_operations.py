# s1 = "Python is fun"
# print(s1[0]) # P
# print(s1[-1]) # n
# print(len(s1)) # 13

# language = "Python"
# version = "3.13.3"
# print(language + version) # Python3.13.3
# # print("Python" - "P") --> unsupported operand type

s1 = "Python"
print(s1 * 3) #PythonPythonPython
# In string, '*' is repetition operator


# Membership operation
# in
s1 = "Python is fun"
print("Python" in s1) # True
print("i" in s1) # True
print("z" in s1) # False
print("Java" in s1) # False


# not in
print("Python" not in s1) # False
print("i" not in s1) # False
print("z" not in s1) # True
print("Java" not in s1) # True



# Comparision of strings
print("Python" == "Python") # True
print("Python " == "Python") # False


# Removing spaces from a string - strip()
s1 = "  Python            "
s2 = s1.strip()
print(s2) # Python
print(s1.strip() == "Python") # True


# replace()
s1 = "We are learning Python"
print(s1) # We are learning Python
print(s1.replace("Python", "java")) # We are learning Java
print(s1.replace("e", "E")) # WE arE lEarning Python
print(s1.replace("e", "E",1)) # WE are learning Python


# Counting substring from a string
# count()
# string.count(substring)
s1 = "We are learning Python. Python is fun."
s2 = "Python"
print(s1.count(s2)) # 2
print(s1.count('e')) # 3
print(s1.count('learn')) # 1
print(s1.count(' ')) # 6


# Changing case of a string
# upper(), lower(), title(), capitalize()
s1 = "We are learning Python"
print(s1.upper()) # WE ARE LEARNING PYTHON
print(s1.lower()) # we are learning python
print(s1.title()) # We Are Learning Python
print(s1.capitalize()) # We are learning python


# startswith()
# string.startswith(substring)
print(s1.startswith("W")) # True
print(s1.startswith("We ")) # True
print(s1.startswith("Python")) # False
print(s1.startswith("are")) # False


# endswith()
# string.endswith(substring)
print(s1.endswith("n")) # True
print(s1.endswith("Python")) # True
print(s1.endswith("We")) # False
print(s1.endswith("learning")) # False
