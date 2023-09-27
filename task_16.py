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

print(count)