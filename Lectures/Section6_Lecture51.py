# Assessment: 08 Functions and Methods Homework

# 1
import math
import re
import string


def vol(rad):
    return (4/3 * math.pi) * rad**3
    pass
    # course solution
    return (4.0/3) * (3.14) * (rad ** 3)

print(vol(2))

# 2
def ran_check(num,low,high):
    in_range = low < num < high
    if in_range:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')

    pass
    # course solution
    if num in range(low, high):
        print(" %s is in th erange" % str(num))
    else:
        print("The number is outside the range.")


ran_check(5,2,7)
ran_check(8,2,7)
ran_check(1,2,7)

# 3
def ran_bool(num,low,high):
    return low < num < high
    pass
    # course solution
    return num in range(low, high)

print(ran_bool(3,1,10))

# 4
def up_low(s):
    num_lows = 0
    num_highs = 0
    alphabet = list(string.ascii_lowercase)
    upper_alphabet = [letter.upper() for letter in alphabet]
    regex = re.compile('[^a-zA-Z]')
    s = regex.sub('', s)
    for letter in s:
        if letter in alphabet:
            num_lows += 1
        else:
            num_highs += 1 # in upper case alphabet

    print(f'No. of Upper case characters : {num_highs}')
    print(f'No. of Lower case characters : {num_lows}')
    pass

    # course solution
    d = {"upper":0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", s)
    print(f'No. of Upper case characters : {d["upper"]}')
    print(f'No. of Lower case characters : {d["lower"]}')

# 5
def unique_list(lst):
    return list(set(lst))
    pass

    # course solution
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# 6
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
    pass

    # course solution
    total = numbers[0]
    for x in numbers:
        total *= x
    return total

print(multiply([1,2,3,-4]))

# 7
def palindrome(s):
    if len(s) %2 != 0:
        return False
    halfway = int(len(s)/2)
    return s[:halfway:] == s[::-1][:halfway:]
    pass

    # course solution
    return s == s[::-1]


print(palindrome('helleh'))
print(palindrome('hello'))



# 8
import re
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    regex = re.compile('[^a-zA-Z]')
    s = regex.sub('', str1.lower())

    found_dict = {}
    for letter in list(alphabet):
        found_count = 1 if letter in s else 0
        found_dict[letter] = found_count

    for letter, found_count in found_dict.items():
        if found_count == 0:
            return False

    return True
    pass

    # course solution
    alphaset = set(alphabet) <= set(str1.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The quick brown fox jumps over the lazy"))