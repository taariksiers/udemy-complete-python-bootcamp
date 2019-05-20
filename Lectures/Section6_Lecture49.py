# Lambda, map and filter functions

def square(num):
    return num ** 2

my_nums = [1,2,3,4,5]

print('List mapped to function\n------------------')
print(list(map(square, my_nums)))

print('\nSplicer\n------------------')

names = ['Andy', 'John', 'Frans']
def splicer(mystring):
    return 'EVEN' if len(mystring) %2 == 0 else mystring[0]

def splicer_a(mystring): return 'EVEN' if len(mystring) %2 == 0 else mystring[0]

splicer_res = list(map(lambda x:x[0], names))

print(f'Original Splicer: {list(map(splicer, names))}')
print(f'Lambda Splicer: {splicer_res}')

print('\nFilter\n------------------')

mynums = [1,2,3,4,5,6]

def check_even(num):
    return num%2 == 0

def check_even_a(num): return num%2 == 0

# lambda with filter
lambda_filtered = list(filter(lambda num: num%2 == 0, mynums))
print(f'Lambda Filtered {lambda_filtered}')

# method must have boolean return
print(f'Original Check even: {filter(check_even, my_nums)}')
print(f'Check even result: {list(filter(check_even, mynums))}')

print('\nLambda\n------------------')
def square(num):
    result = num ** 2
    return result

    pass
    # step 1 to lambda this function
    return num ** 2

    # step 2 - make it a 1 liner
    # def square(num): return num ** 2

    # step 3
    # lambda num: num ** 2

print(f'Square Original: {square(3)}')

# 1 option
square_l = lambda num: num ** 2
print(f'Square L: {square_l(3)}')

# another option
lambda_list = list(map(lambda num: num ** 2, mynums))
print(f'One liner: list(map(lambda num: num ** 2, mynums))) : {lambda_list}')


