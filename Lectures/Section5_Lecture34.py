print("For loops in python\n------------------")
mylist = 'Hello'

for letter in mylist:
    print(f"Cool {letter}!")

for _ in mylist: # not using the variable
    print('Cool!')

print("\nDealing with tuples in lists\n-----------------")
tup = (1,2,3)
for item in tup:
    print(item)

# tuple pairs in a list - tuple unpacking
mylist = [(1,2,3), (3,4,5), (5,6,7), (7,8,9)]


for item in mylist:
    print(item)

for a,b,c in mylist:
    print(b)
    # access to individual items - tuple unpacking

print("\nDealing with dictionaries\n-------------")
d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item) # prints value

for item in d.items():
    print(item) # prints whole key-value

for key,value in d.items():
    print(f"{key}<--->{value}")