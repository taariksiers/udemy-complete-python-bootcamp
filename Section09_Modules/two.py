# two.py

import one

print('TOP LEVEL in two.py')

one.func()

if __name__ == '__main__':
    # run the script
    print('TWO.py is being run directly!')
else:
    print('TWO.py is being imported')