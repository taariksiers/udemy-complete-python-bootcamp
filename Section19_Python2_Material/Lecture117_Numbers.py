# Lecture 117

# Types of numbers - integers and floating point numbers (exponential or decimal)
# python2 classical division, rounds off. Python 3 true division
print("Types of numbers\n==================\n")
print("3/2")
print(3/2) 
print("3.0/2")
print(3.0/2)
# print("cast float(3)/2")
print('Cast float(3)/2 %(value)f' % {'value': float(3)/2})  # 1.50000
print('Cast float(3)/2 {0} | {1}' . format(float(3)/2, 'ah yeah')) # 1.5

# from __future__ import division # now treats division like python 3

# order of operations
print("\nOrder Of Operations\n======================\n")
print('2 + 10 * 10 + 3 = {0}' . format(2 + 10 * 10 + 3,))
print('(2+10) * (10+3) = {0}' . format((2+10) * (10+3),))

# assigning labels to objects
# rules, cannot start with a number, no spaces, excluded symbols
print("\nAssigning Labels\n==============\n")
a = 5
print('a = {0}. Now declare a = 10' . format(a,))
a = 10
print('a = {0}' . format(a,))
print('a+a = {0}' . format(a+a,))
