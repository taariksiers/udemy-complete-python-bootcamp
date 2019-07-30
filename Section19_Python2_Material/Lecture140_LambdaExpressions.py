# create anonymous / ad-hoc function - for simple functionss
# start off with standard def and refine

def square(num):
    result = num**2
    return result

print 'square(2)={n}' . format(n=square(2))

def square2(num):
    return num**2

print 'square2(2)={n}' . format(n=square2(2))

def square3(num): return num**2

print 'square3(2)={n}' . format(n=square3(2))

square4 = lambda num: num**2
print 'square4 = lambda num: num**2' . format(n=square4(2))
even = lambda num: num % 2 == 0
print 'even = lambda num: num % 2 == 0 - 10 | {n}' . format(n=even(10))
print 'even = lambda num: num % 2 == 0 - 11 | {n}' . format(n=even(11))

first_char = lambda string: string[0]
print 'first_char = lambda string: string[0] - \'hello\' | {f}' . format(f=first_char('hello'))

rev = lambda s: s[::-1]
print 'rev = lambda s: s[::-1] - \'Hello\' | {f}' . format(f=rev('Hello'))

# multiple arguments

def adder(x,y):
    return x+y

print 'adder 10,11 = {n}' . format(n=adder(10,11))

adder2 = lambda x,y: x+y
print 'adder2 = lambda x,y: x+y - 11, 13 | {n}' . format(n=adder2(11,13))

thelen = lambda item: len(item)
the_string = 'hello over there'
print 'thelen = lambda item: len(item) - \'{s}\' |  {n}' . format(s=the_string,n=thelen(the_string)) 
