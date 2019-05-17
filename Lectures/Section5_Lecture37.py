# List comprehension
mystring = 'hello'

mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)
# ['h', 'e', 'l', 'l', 'o']

# OR

mylist = [letter for letter in mystring]
print(mylist)
# ['h', 'e', 'l', 'l', 'o']

mylist = [x for x in 'word'] # var for var in object/string
print(mylist)
# ['w', 'o', 'r', 'd']

mylist = [num for num in range(0,11)]
print(mylist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist = [num**2 for num in range(0,11)] # flattening out the for loop
print(mylist)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist = [num for num in range(0,11) if num%2 == 0]
print(mylist)
# [0, 2, 4, 6, 8, 10]

mylist = [num**2 for num in range(0,11) if num%2 == 0]
print(mylist)
# [0, 4, 16, 36, 64, 100]

celcius = [0, 10, 20, 34.5]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
# [32.0, 50.0, 68.0, 94.1]

# if else order is different versus earlier usage with just if
results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)
# [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

mylist = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)

print(mylist)
# [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

# same as above
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)
# [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

for num in list(range(1,100)):
    output = ''
    if num%3 == 0:
        output += 'Fizz'
    if num % 5 == 0:
        output += 'Bizz'
    if len(output):
        print(f"{output} {num}")
