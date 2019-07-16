# Counter
from collections import Counter

print('Counter\n========================\n')
l = [1,1,2,3,1,1,3,4,5]
print(f'Before {l}')
print(f'After Counter(l) {Counter(l)}\n')
 
s = 'sdlafkjdfklj12j1230ujlkjlfkja'
print(f's={s}')
print(f'Counter(s) {Counter(s)}\n')

s = 'How many times does each word show up in this sentence show show up up'
print(f's={s}')

words = s.split()
c = Counter(words)
print(f'Counter(words) words=s.split() {c}\n')

print(f'c.most_common(3) {c.most_common(3)}')
print(f'sum(c.values()) {sum(c.values())}')

print(f'list(c) {list(c)}')


