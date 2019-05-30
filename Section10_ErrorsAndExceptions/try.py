try:
    result = 10 + 10
    # WANT TO HAPPEN
except:
    print('Error!')
    # Exception handling
else:
    print('It worked')
finally:
    result = 0 if 'result' not in locals() or 'result' not in globals() else result
    print('All done')
    # and do always

print(f'Result is {result}')

print(f'\n{"-" * 100}\n')

try:
    f = open('testfile.txt', 'w')
    f.write('Write a test line\n')
except TypeError:
    print('there was a type error')
# except OSError:
except:
    print('ALL: hey you have an os error')
finally:
    print('I always run')


print(f'\n{"-" * 100}\n')

def ask_for_int():
    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print('Yes thanks')
            break
        finally:
            # print('End of try/except/finally\n--x-x--')
            print('Re-requesting...\n--x--x--')

ask_for_int()

