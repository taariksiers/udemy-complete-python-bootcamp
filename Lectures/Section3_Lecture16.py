print("String properties and methods")
name = "Sam"
print(name)
# name[0] = "P" # TypeError: 'str' object does not support item assignment
last_letters = name[1:]
print("P" + last_letters)

x = "Hello World"
x = x + " it is beautiful outside"
print(x)

letter = "z"
print(letter * 10)

print("\nint type 2 +  int type 3 ")
print(2+3)
print("string type 2 +  string type 3 ")
print("2" + "3")

x = "Hello World"
print("\nString Test: " + x + "\nx.upper(): " + x.upper())
print("\nString split by space x.split(): ")
print(x.split()) # default on whitespace

x = "Hi this is a string"
print("\nString split by space x.split('i'): " + x)
print(x.split('i'))


