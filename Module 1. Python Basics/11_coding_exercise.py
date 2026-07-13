# Area of triangle

"""
When all the length of the sides of the triangle is known - a, b, c
Semi perimeter (S) = (a + b + c) / 2
Area = square root of (s * (s - a) * (s - b) * (s - c))
"""

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of triangle with given sides is", round(area, 2))



# Simple Interest

"""
Simple interest = (P * R * T) / 100
P = Principle amount
R = Rate of interest
T = time duration
"""

P = float(input("Enter principle amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time duration: "))
SI = (P * R * T) / 100
print("The Simple Interest is",SI)



# Compound Interest

"""
P = Principle amount
R = Rate of interest
T = time duration
Amount = P(1 + R/100) ** T
Compound interest = Amount - P
"""

P = float(input("Enter principle amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time duration: "))
amount = P * pow((1 + (R / 100)), T)
print("Amount is", round(amount, 2))
CI = amount - P
print("Compound interest is", round(CI,2))