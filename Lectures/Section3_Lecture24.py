print("Tuple + List")
t = (1,2,3)
my_list = [1,2,3]

print("Tuple + type(t): ", t, type(t))
print("List + type(my_list): ", my_list, type(my_list))

t = ('a', 'a', 'b')
print("\nNew Tuple: ", t)
print("Count 'a' | t.count('a') : ", t.count('a'))
print("Index 'a' (first occurrence) | t.index('a') : ", t.index('a'))
print("Index 'b' | t.index('b') : ", t.index('b'))

my_list[0] = 'NEW'
print("\nBack to my_list | my_list[0] = 'NEW' : ", my_list)

# try to do with a tuple
# t[0] = 'd' # object does not support item assignment