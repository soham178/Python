# \n - new/next line
# \t - tab
# \\ - backslash
# \' - inserts a single quote inside a single-quated string



#<-----\n----->

print("Hello everyone.\nHow are you?")
# Hello everyone.
# How are you?


#<-----\t----->

print("John 20") # John 20
print("John\t20") # John    20


#<-----\\----->

print("new\old") # it prints but new\old gives an warning that it's an invalid escape sequence
print("new\\old") # new\old


#<-----\'----->

# print('This is Python's class') --> error (unterminated string literal)
print('This is Python\'s class') # This is Python's class


#<-----\"----->

print("He says, \"we are learning Python\"")
# He says, "we are learning Python"