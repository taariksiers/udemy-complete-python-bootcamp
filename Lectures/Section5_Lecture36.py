# Useful operators in python
print("Range\n------------------")

for num in range(0,10):
    print(num)

print("Range with step\n------------------")

for num in range(0,11,2):
    print(num)

list(range(0,11,2))

print("Enumerate\n------------------")

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}' . format(index_count, letter))
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item) # print a tuple, so you could tuple unpack

for index, letter in enumerate(word): # tuple unpacking
    print(f"{index}<-- I L -->{letter}")

print("ZIP\n------------------")
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']

# can only zip as far as shortest list
for item in zip(mylist1, mylist2):
    print(item) #output of tuples

print("IN\n------------------")
d = 'x' in [1,2,3] # list
e = 'x' in [1, 'x', 3]
g = 'r' in 'a world' # string
f = 'mykey' in {'mykey' : 'hi'} # dictionary
h = 'hi' in {'mykey' : 'hi'} # dictionary
i = 'hi' in {'mykey' : 'hi'}.values() # dictionary values

print(f"list {e} {d} | string {g} | dictionary {f} {h} {i}")

print("Math type\n------------------")
mylist = range(1,10)
print(min(mylist))
print(max(mylist))
print(sum(mylist))

from random import shuffle
a = list(mylist)
shuffle(a)
print(a)

from random import randint
print(randint(0,100))

print("User input\n------------------")

result = input('What is your name? ')
print(f"Hello {result}")

result = int(input('What is your favourite number? '))
print(f"Hello {result}")

