def test(n):
    if n == 0:
        return 0
    if n > 0 and n%2 == 0:
        return test(n/2)
    if n%2 != 0:
        return 1 + test(n-1)


count = 0
for x in range(1, 1001):
    if test(x) == 3:
        count += 1

# print(count)

import sys

sys.setrecursionlimit(10**6)

def f16(n):
    if n == 1:
        return 1
    
    return n - 1 + f16(n - 1)

# print(f16(2024) - f16(2022))