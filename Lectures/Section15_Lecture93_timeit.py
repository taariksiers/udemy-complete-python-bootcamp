# 93 timeit - Timing your code
import timeit

# '0-1-2-3-....-99'
print(f'"-".join(str(n) for n in range(100)\n{"-".join(str(n) for n in range(100))}\n')

timeit.timeit("-".join(str(n) for n in range(100)), number=1000000)

print(f'timeit.timeit("-".join(str(n) for n in range(100)), number=1000000) ---> {timeit.timeit("-".join(str(n) for n in range(100)), number=1000000)}\n')
print(f'timeit.timeit("-".join([str(n) for n in range(100)]), number=1000000) ---> {timeit.timeit("-".join([str(n) for n in range(100)]), number=1000000)}\n')
print(f'timeit.timeit("-".join(map(str,range(100))), number=1000000) ---> {timeit.timeit("-".join(map(str,range(100))), number=1000000)}\n')
