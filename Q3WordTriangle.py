# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON

A = str(input())
B = len(A)

for value in range(B):
    print(A[0:value])
print(A)