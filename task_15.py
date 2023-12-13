def f():
    c = 0
    for a in range(100):
        f = True
        for x in range(100):
            for y in range(300):
                if ((x > a) and (x * x <= a)) or ((y * y >= a) and (y < 5)):
                    f = False
                    
        if f:
            c += 1

    return c

print(f())


def f7_1():
    o = [2, 4, 6, 8, 10, 12]
    p = [3, 6, 9, 12, 15]
    a = []

    for x in range(100):
        if (not(x in o) or (not(x in p) <= (x in a)) ) != 1:
            a.append(x)
            
    import math
    print(math.prod(a))
    

# Какую наибольшую длину может иметь отрезок A?
def f():
    a = [x for x in range(-10000, 10000)]

    for x in range(-10000, 10000):
        if (((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))) != 1:
                a.remove(x)

    print(len(a) - 1)
    