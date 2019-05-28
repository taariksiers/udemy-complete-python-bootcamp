# one.py

def func():
    print('FUNC() in one.py')


print('Top level in ONE.PY')

if __name__ == '__main__':
    # run the script
    print('ONE.py is being run directly!')
else:
    print('ONE.py is being imported')