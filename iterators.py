# Zadanie 7.6
import itertools
import random

iter1 = itertools.cycle([1, 0])

for i in range(10):
    print(next(iter1))


print("")

iter2 = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))

for i in range(10):
    print(next(iter2))

print("")
iter3 = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

for i in range(10):
    print(next(iter3))