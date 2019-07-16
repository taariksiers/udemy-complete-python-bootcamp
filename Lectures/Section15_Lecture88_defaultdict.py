from collections import defaultdict

print('defaultdict\n====================\n')

d = {'k1':1}
print(f"d {d} d['k1'] {d['k1']}\n")

try:
    print(f"d['k2'] results in KeyError")
    print(f"{d['k2']}")
except KeyError:
    print('Key error encountered\n')

d = defaultdict(object)
d['one']   

print(f"d = defaultdict(object)\nd['one'] {d['one']}")
for item in d:
    print(item)

print(f"\nd['2'] {d['2']}")

d['two']= 2
print(f"d['two']={d['two']}\nd {d}")
