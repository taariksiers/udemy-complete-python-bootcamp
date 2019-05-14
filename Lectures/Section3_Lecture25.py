my_set = set()
print("my_set: ", my_set, type(my_set))
my_set.add(1)

print("my_set.add(1): ", my_set) # looks like a dictionary

my_set.add(2)
print("my_set.add(2): ", my_set)

my_set.add(2)
print("my_set.add(2): ", my_set) # maintains unique values

# possible usefulness, casting from list to set
my_list = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
print("my_list: ", my_list, type(my_list))
set(my_list)
print("set(my_list): ", set(my_list)) # in place

b = None
print("b: ", b)