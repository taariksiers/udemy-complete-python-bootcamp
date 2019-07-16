from collections import OrderedDict
print(f'OrderDict\n========================\n')

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(f'd {d}\ntype {type(d)}\nFor Loop:')

for k,v in d.items():
    print(f'{k} {v}')

print('\n') 

e = OrderedDict()
e['a'] = 1
e['b'] = 2
e['c'] = 3
e['d'] = 4
e['e'] = 5
print(f'e {e}\ntype {type(e)}\nFor Loop:')
for k,v in e.items():
    print(f'{k} {v}')

print('\n') 

d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(f'Type differences: d1 type {type(d1)} {d1}\nd2 type {type(d2)} {d2}\nd1 == d2 {d1 == d2}')

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(f'Type differences: d1 type {type(d1)} {d1}\nd2 type {type(d2)} {d2}\nd1 == d2 {d1 == d2}')
