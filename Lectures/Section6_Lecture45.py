# 03 Function Practice Exercises Assessment

# 1
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return a if b > a else b
    return a if a > b else b

    pass

    # SOLUTION
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

# 2
def animal_crackers(text):
    words = text.split()
    return words[0][0].lower() == words[1][0].lower()

    pass

    # SOLUTION
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


# 3
def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    if n1 == 20 or n2 == 20:
        return True
    return False

    pass

    # SOLUTION
    return (n1+n2)==20 or n1==20 or n2==20


# 4
def old_macdonald(name):
    new_name = [letter for letter in name.lower().capitalize()]
    new_name[3] = new_name[3].upper()

    return ''.join(new_name)

    pass
    # SOLUTION

    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


# 5
def master_yoda(text):
    yoda = text.split()
    yoda.reverse()

    return ' '.join(yoda)

    pass

    # SOLUTION
    return ' '.join(text.split()[::-1])

# 6
def almost_there(n):
    return 110 > n > 90 or 210 > n > 190

    pass

    # SOLUTION
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# 7
def has_33(nums):
    last_value = None
    for num in nums:
        if last_value == None:
            last_value = num
            continue

        if last_value == num:
            return True

        last_value = num

    return False

    pass

    # SOLUTION
    for i in range(0, len(nums) - 1):

        # nicer looking alternative in commented code
        # if nums[i] == 3 and nums[i+1] == 3:

        if nums[i:i + 2] == [3, 3]:
            return True

    return False


# 8
def paper_doll(text):
    new_text = ''
    for letter in text:
        new_text += letter * 3

    return new_text

    pass

    # SOLUTION
    result = ''
    for char in text:
        result += char * 3
    return result

# 9
def blackjack(a,b,c):
    if a + b + c <= 21:
        return a + b + c
    if a + b + c > 21 and a == 11 or b == 11 or c == 11:
        return (a + b + c) - 10
    else:
        return 'BUST'

    pass

    # SOLUTION

    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

# 10
def summer_69(arr):
    summing = 0
    ignore = False

    for num in arr:
        if num == 6 or num == 9:
            ignore = num == 6
            continue

        if ignore:
            continue

        summing += num

    return summing

    pass

    # SOLUTION
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

# 11
def spy_game(nums):
    build_string = '007'
    return_string = ''
    for num in nums:
        if len(return_string) == 3:
            break

        if len(return_string) == 0 and num == 0:
            return_string += str(num)
            continue
        if len(return_string) == 1 and num == 0:
            return_string += str(num)
            continue
        if len(return_string) == 2 and num == 7:
            return_string += str(num)
            continue

    return return_string == build_string

    pass

    # SOLUTION
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1


# 12
def spy_game(nums):
    build_string = '007'
    return_string = ''
    for num in nums:
        if len(return_string) == 3:
            break

        if len(return_string) == 0 and num == 0:
            return_string += str(num)
            continue
        if len(return_string) == 1 and num == 0:
            return_string += str(num)
            continue
        if len(return_string) == 2 and num == 7:
            return_string += str(num)
            continue

    return return_string == build_string

    pass

    # SOLUTION
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

    # SOLUTION 2
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

