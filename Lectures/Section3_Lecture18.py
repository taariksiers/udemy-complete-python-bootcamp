print("\n====== Section 3, Lecture 18 ======== ")
print('This is a string {}' . format('INSERTED')) # standard
print('No indexing: The {} {} {}' . format('fox', 'brown', 'quick'))
print('Numerical indexing: The {2} {1} {0}' . format('fox', 'brown', 'quick'))
print('Numerical indexing: The {0} {0} {0}' . format('fox', 'brown', 'quick'))
print('Keyword assignment: The {q} {b} {f}' . format(f='fox', b='brown', q='quick')) # inserted by index
print('Keyword assignment: The {b} {q} {f}' . format(f='fox', b='brown', q='quick'))

result = 100/777

print("\nFloat formatting: result 100/777 = {}" . format(result))
print("Float formatting: result 100/777 = {r}" . format(r=result))
print("Float formatting: result 100/777 = {r:5.1f}" . format(r=result)) # value:width.precision - width, how long / wide you want the string to be
print("Float formatting: result 100/777 = {r:1.5f}" . format(r=result)) # value:width.precision - width, how long / wide you want the string to be

name = "Sam"
age = "3"
print(f'\nHello my name is {name} and I am {age} years old')