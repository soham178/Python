s1 = "Hello World"

"""
Syntax of indexing: string[index]
Syntax of indexing: string[start:end:step]
- start: starting idex at which the slicing operation starts
- end: ending index at which the slicing stops (excluded)
-step: integer that specifies the step for the slicing
"""

print(s1[2:7:1]) # llo W
print(s1[2:9:2]) # loWr
print(s1[1:12:3]) # eood