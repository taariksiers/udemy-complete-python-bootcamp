def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}' . format(args[0], kwargs['food']))


# must be args in a row and kwargs in a row, no random ordering
myfunc(10,20,30,fruit='orange',food='pizza',animal='dog')
