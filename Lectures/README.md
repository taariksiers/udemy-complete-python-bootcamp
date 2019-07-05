# Section 3

## Lecture 14

- Strings are ordered sequences of characters.
- This means you can use indexing and slicing to grab sub-sections of the string.

## Lecture 18
- Stick/inject a variable into a string - string interpolation
- f-strings - formatted string literals 

```
name = 'Jack'
lastname = 'Bauer'
print(f"Hello, my name is {name} {lastname}")
```

## Lecture 20

### Lists
- **Lists** are **ordered** sequences that can hold a *variety* of **object types**
- They use [] brackets and commas to separate objects, e.g. `[1,2,3,4,'a']`
- Lists support indexing and slicing i.e. retrieve based on location
- They can be nested and also have a variety of methods that can be called off them
- Can mutate values, add values (append), or remove (pop), reverse, sort

## Lecture 22

### Dictionaries
- Dictionaries are **unordered mappings** for storing objects. They cannot be sorted.
- Dictionaries use key-value pairing `{'key1':'value1', 'key2','value2'}`
- Useful because you can grab based on key
- Can hold different data types and even dictionaries
- Keys should always be strings

## Lecture 24

### Tuples
- Very similar to lists, however, one key difference - **immutability**
- Once an element is inside a tuple, it cannot be reassigned
- Tuples use parenthesis: `(1, 2, 3)`
- Supports indexing, slicing

## Lecture 25

### Sets
- Sets are **unordered** collections of **unique** elements
- There can only be 1 representative of the same object `my_set = set(1,3,4)`

## Lecture 26

### Booleans
- **False** and **True** (case is important)
- You can also use the **None** placeholder when declaring a variable `b = None`

# Section 4

## Lecture 31

### Comparison Operators
`> == != <=`

## Lecture 32

### Logical & Chain Operators

`and or not`

# Section 5

## Lecture 33/34/35 - Control flow statements

`if elif else for while pass continue break`
`range enumerate zip in`

### Lecture 37 - List Comprehensions

# Section 6 - Methods and Built In Objects

## Arguments and Keyword Arguments

- args - tuple  - *
- kwargs = keyword args - dictionary - **

## Scope Resolution

### LEGB Rule
- Local names within a function (def or lambda) - and not global
- Enclosing function locals - names in the local scope of any enclosing functions def or lambda from inner to out
- Global - names assigned at the top level of a module file or declared global in a def within the file
- Built-in (Python)

# Section 12 - Python Decorators

```
def new_decorator(original_func):
    ...

@new_decorator
def func_needs_decorator():
    ...
```