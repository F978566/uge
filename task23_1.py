res = set()
def f(a, c):
    global res
    if c == 6:
        res.add(a)
    else:
        f(a + 1, c + 1)
        f(a + 2, c + 1)
        f(a * 2, c + 1)


f(1, 0)
print(res)
a = [x for x in range(34, 60 )]
print(len([x for x in res if x in a]))