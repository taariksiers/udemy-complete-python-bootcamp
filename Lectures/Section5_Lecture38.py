# Assessment

st = 'Print only the words that start with s in this sentence'
starters = [word for word in st.split() if word[0].lower() == 's']
print(starters)

# Use range() to print all the even numbers from 0 to 10
result = [num for num in range(0,10) if (num > 0 and num%2==0)]

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
result = [num for num in list(range(1,50)) if num%3==0]

st = 'Print every word in this sentence that has an even number of letters'
result = [word for word in st.split() if len(word) %2 == 0]

# Fizz Buzz
for num in list(range(1,101)):
    output = ''
    if num%3 == 0:
        output += 'Fizz'
    if num % 5 == 0:
        output += 'Bizz'
    if len(output):
        print(f"{output} {num}")
    else:
        print(num)


st = 'Create a list of the first letters of every word in this string'
result = ''.join([word[0] for word in st.split()])
