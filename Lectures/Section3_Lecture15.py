print("String Indexes")
print("---------------")

mystring = "Hello World"

print("Original: " + mystring)
print("Indices 0:" + mystring[0] + " | 6:" + mystring[6] + " | 9:" + mystring[9] + " | -3:" + mystring[-3])

print("\nString Slicing")
print("---------------")

mystring = "abcdefghijk"
# start index, stop index, step size(default 1)
print("Original: " + mystring)
print("Slicing [2:] " + mystring[2:])
print("Slicing [:3] " + mystring[:3])
print("Slicing [3:6] " + mystring[3:6])
print("Slicing [1:3] " + mystring[1:3])
print("Slicing + step sizing | [::2] " + mystring[::2])
print("Slicing + step sizing | [::3] " + mystring[::3])
print("Slicing + step sizing: Reverse a string | [::-1] " + mystring[::-1])
