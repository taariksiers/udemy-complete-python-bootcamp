my_list = [1,2,3]

print("List 1 - same types")
print(my_list)

my_list = ['STRING', 100, 23.2]
print("\nList 2 - mixed types and length")
print(my_list)

print(len(my_list))

print("\nIndexing and Slicing: Full List and my_list[1]")
my_list = ['one', 'two', 'three']
print(my_list)
print(my_list[1])

another_list = ['four', 'five', 'six']

print("\nanother_list for concatenation = new_list")
new_list = my_list + another_list
print(new_list)
print("Changing/mutate first element new_list[0] = 'ONE ALL CAPS'")
new_list[0] = 'ONE ALL CAPS'
print(new_list)

print("\nnew_list.append('Seven')")
new_list.append('Seven')
print(new_list)

print("\nnew_list.pop() and print pop_value")
pop_value = new_list.pop()
print(new_list)
print(pop_value)

print("\nnew_list.pop(1) and print pop_value")
pop_value = new_list.pop(0)
print(new_list)
print(pop_value)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

print("\nList sorting with .sort() IN PLACE : new_list & num_list")
print(new_list)
print(num_list)
new_list.sort()
num_list.sort()
print("Sorted")
print(new_list)
print(num_list)

print("Reverse: also done in place")
new_list.reverse()
num_list.reverse()
print(new_list)
print(num_list)

print("\nIndex a nested list [1,1,[1,2]] and get the value 2 my_list[2][1]")
my_list = [1,1,[1,2]]
print(my_list[2][1])