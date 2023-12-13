"""
Текстовый файл состоит из символов T, U, V, W, X, Y и Z.

Определите в прилагаемом файле максимальное количество идущих подряд
символов (длину непрерывной подпоследовательности),
среди которых символ T встречается ровно 100 раз.

Для выполнения этого задания следует написать программу.
"""

def f():
    with open('f.txt', 'r') as f:
        rf = f.readline()
    
    pointer1 = 0
    pointer2 = 1
    
    c = 1
    maxx = -1000

    l = 0
    
    while pointer1 < pointer2 and pointer2 < len(rf):
        if rf[pointer2] == 'T':
            c += 1
        
        if c == 100:
            maxx = max(maxx, l)
            while c == 100:
                if rf[pointer1] == 'T':
                    c -= 1

                pointer1 += 1
                l -= 1
        
        pointer2 += 1
        l += 1

    print(maxx)
    
f()