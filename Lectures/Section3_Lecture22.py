my_dict = {'key1': 'value1', 'key2': 'value2'}
print("my_dict with my_dict[key1]")
print(my_dict)
print(my_dict['key1'])

print("\nPrices lookup dictionary and get apple price")
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup)
print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0,1,2], 'k3' : {'insideKey':100}}
print("\nDictionary inside a dictionary d['k2'] and d['k3']['insideKey'] and d['k2'][2]")
print(d)
print(d['k2'])
print(d['k3']['insideKey'])
print(d['k2'][2])

# long form convert last letter to upper case
d = {'key1' : ['a', 'b', 'c']}
print("\nNew dictionary")
print(d)
mylist = d['key1']
letter = mylist[2]
print("Upper Case the long way: ", letter.upper())

# short form
print("Upper Case the short way: d['key1'][2].upper() - ", d['key1'][2].upper())

d = {'k1' : 100, 'k2' : 200}
print("\nNew Dictionary add d['k3'] = 300, override d['k1'] = 'NEW VALUE'")
print("full d : ", d)
d['k3'] = 300
print("d['k3'] = 300: ", d)
d['k1'] = 'NEW VALUE'
print("d['k1'] = 'NEW VALUE: ", d)

d = {'k1': 100, 'k2': 200, 'k3': 300}
print("\nNew dictionary: print keys, values & items")
print(d)
print("keys  : ", d.keys())
print("values: ", d.values())
print("items : ", d.items())
