print('Problem One:')
for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print(f'Incorrect type provided \'{i}\'')

print(f'\n{"-" * 100}\nProblem Two:')

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print(f'Cannot divide {x} by {y}')
finally:
    print('All Done.')

print(f'\n{"-" * 100}\nProblem Three:')

def ask():
    """Take a number(type int) as input and square it"""
    result = 0
    while True:
        try:
            num = int(input('Please provide a number: '))
        except:
            print('An error occured! Please try again!')
            continue
        else:
           result = num**2
           break
        finally:
            pass

    return result


result = ask()
print(f'Squared = {result}')
# help(ask)
