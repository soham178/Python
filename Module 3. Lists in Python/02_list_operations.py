# Slicing of lists
l1 = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(l1[1:6:1]) # [8, 1, 0, 4, 9]
print(l1[0:8:2]) # [3, 1, 4, 7]


# Concatenation of lists
l1 = [1, 7, 2]
l2 = [0, 5]
print(l1 + l2) # [1, 7, 2, 0, 5]
print(l2 + l1) # [0, 5, 1, 7, 2]


# Repetition of list
print(l2 * 3)
#[0, 5, 0, 5, 0, 5]


# append() => adds an item to the end of the list
fruits = ["Mango", "Apple", "Orange"]
# Syntax: list.append(item)
fruits.append("Banana")
print(fruits) # ['Mango', 'Apple', 'Orange', 'Banana']
print(fruits.append("watermelon")) # None
# append fuction does not return the updated list....it just update the list


# insert() => adds an element before the specified index
# Syntax: list.insert(index, item)
fruits = ["Mango", "Apple", "Orange"]
fruits.insert(2, "Banana")
print(fruits) # ['Mango', 'Apple', 'Banana', 'Orange']


# extend()
fruits = ["Mango", "Apple", "Orange"]
# fruits.append("Banana", "Grapes")
# print(fruits) # error
# list.append() takes exactly one argument
fruits.extend(["Banana", "Grapes"])
print(fruits) # ['Mango', 'Apple', 'Orange', 'Banana', 'Grapes']
print(len(fruits)) # 5

fruits = ["Mango", "Apple", "Orange"]
fruits.append(["Banana", "Grapes"])
print(fruits) # ['Mango', 'Apple', 'Orange', ['Banana', 'Grapes']]
print(len(fruits)) # 4


# remove()
fruits = ["Mango", "Apple", "Orange"]
fruits.remove("Mango")
print(fruits) # ['Apple', 'Orange']

fruits = ["Apple", "Mango", "Orange", "Mango"]
fruits.remove("Mango")
print(fruits) # ['Apple', 'Orange', 'Mango']


# pop()
fruits = ["Apple", "Mango", "Orange", "Mango"]
fruits.pop(2)
print(fruits) # ['Apple', 'Mango', 'Mango']

fruits = ["Apple", "Mango", "Orange", "Mango"]
fruits.pop()
print(fruits) # ['Apple', 'Mango', 'Orange']


# reverse()
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_of_week.reverse()
print(days_of_week)
# ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']


# sort()
nums = [4, 9, 0, 1, 2, 8]
nums.sort()
print(nums) # [0, 1, 2, 4, 8, 9]

nums = [4, 9, 0, 1, 2, 8]
nums.sort(reverse=True)
print(nums) # [9, 8, 4, 2, 1, 0]


# count()
nums =  [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(nums.count(0)) # 5
print(f"The list is: {nums}")
item_t0_count = int(input("Enter the number to be counted from the above list: "))
c = nums.count(item_t0_count)
print(f"Occurrence of {item_t0_count} is {c}")
# Occurrence of 0 is 5
# Occurrence of 2 is 0


# Membership operation => in / not in
language = ["Python", "Java", "C++", "Python"]
print("Python" in language) # True
print("Javascript" in language) # False

print("Python" not in language) # False
print("Javascript" not in language) # True