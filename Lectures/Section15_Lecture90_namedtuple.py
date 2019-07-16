from collections import namedtuple
print(f'namedtuple\n===================\n')

t = (1,2,3)
print(f't type {type(t)} {t} t[0] {t[0]}\n')

Dog = namedtuple('Dog', 'age breed name')
print(f'Dog type {type(Dog)}\n')

sam = Dog(age=2,breed='Husky',name='same')
print(f'sam {sam} | type {type(sam)} | sam.age {sam.age} | sam.count {sam.count}\n')

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur='Fuzzy',claws=False,name='Kitty')
print(f"Cat = namedtuple('Cat', 'fur claws name') {Cat} | type {type(Cat)} | c.fur {c.fur} | c.index {c.index}\n")
