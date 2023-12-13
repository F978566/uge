def f27():
    with open('text.txt', 'r') as f:
        rf = f.readlines()
    
    drf = list(map(int, rf))
    
    l = drf[0]
    numbers = drf[1:]
    
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_6 = 0
    count_12 = 0
    
    for x in numbers:
        if x % 12 == 0:
            count_12 += 1
        elif x % 6 == 0:
            count_6 += 1
        elif x % 4 == 0:
            count_4 += 1
        elif x % 3 == 0:
            count_3 += 1
        elif x % 2 == 0:
            count_2 += 1
        else:
            count_1 += 1
            
    k = 0
    
    k += count_12 * (count_12 - 1) // 2
    k += count_12 * (count_6 + count_4 + count_3 + count_2 + count_1)
    k += count_6 * (count_6 - 1) // 2
    k += count_6 * (count_4 + count_2)
    k += count_4*count_3

    print(k)


def f27_1():
    with open('f.txt', 'r') as f:
        l = f.readline()
        rf = f.readlines()
        
    dl = int(l)
    
    summ = 0
    min_rez = 10**10
    
    for x in rf:
        a, b = map(int, x.split())
        
        summ += max(a, b)
        if abs(a - b) % 3 != 0:
            min_rez = min(min_rez, abs(a - b))
        
    if summ % 3 != 0:
        print(summ)
    else:
        print(summ - min_rez)