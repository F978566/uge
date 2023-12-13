def f():
    # with open('f.txt', 'r') as f:
    #     rf = f.readline()
    
    
    rf = 'GGBBCWYBCAHBYBAHCBYABCHBYKJBACYKACBYAKSB'

    nrf = rf.split('Y')
    
    print(nrf)
    
    summ1 = 0
    maxx = 0
    #151 = 7
    for x in range(4):
        summ1 += len(nrf[x])
    summ1 += 3 # 150 = 6
    maxx = summ1

    for x in range(4, len(nrf)):
        summ1 += len(nrf[x]) - len(nrf[x - 4])
        # print(nrf[x])
        # print(nrf[x - 1])
        # print(nrf[x - 2])
        # print(nrf[x - 3])
        # print(nrf[x - 4])
        maxx = max(maxx, summ1)
    print(maxx)

f()


"""Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего
не более 106 символов. Определите максимальное количество идущих подряд символов, среди которых нет букв Y,
а количество точек не превышает 5. """
def f():
    with open('f.txt', 'r') as f:
        rf = f.readline()
    

    nrf = rf.split('Y')
    print(nrf)

    maxx = 0

    for el in nrf:
        if el.count('.') <= 5:
            maxx = max(maxx, el.count('.'))
        else:
            s = el.split('.')
            for x in range(len(s) - 5):
                if len(s[x] + s[x+1] + s[x+2] + s[x+3] + s[x+4] + s[x+5]) > maxx:
                    maxx = len(s[x] + s[x+1] + s[x+2] + s[x+3] + s[x+4] + s[x+5])
    
    print(maxx+5)

# f()


"""
Текстовый файл состоит не более чем из 106 символов латинского алфавита.
Определите минимальную подстроку, содержащую 210 символов "T". Для выполнения
этого задания следует написать программу.

Для выполнения этого задания следует написать программу
"""

def f():
    with open('f.txt', 'r') as f:
        rf = f.readline()
    
    # rf = 'BCJATJHABCJHATCJAVSCTBACHTJHGTVATAJTJATJ'
        
    nrf = rf.split('T')
    
    count = 0
    minn = 0
    
    for x in range(1, 210):
        count += len(nrf[x])
    
    minn = count
    count = 0
    
    for x in range(210, len(nrf)):
        count = 0
        for i in range(209):
            count += len(nrf[x-i])
        minn = min(minn, count)
    
    print(minn+210)


# f()

"""
Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
Определите в прилагаемом файле максимальное количество идущих подряд
символов (длину непрерывной подпоследовательности), среди которых пара
символов W встречается ровно 100 раз.
"""
def f():
    with open('f.txt', 'r') as f:
        rf = f.readline()
    
    ww = [x for x in range(len(rf) - 1) if rf[x] + rf[x+1] == 'WW']
    print(max([ww[x + 102] - ww[x] for x in range(len(ww) - 102)]))
    
"""самый заебатый способ"""
def f():
    with open('f.txt', 'r') as f:
        rf = f.readline()
    
    # rf = 'JBJZJBZKHZHZHZHZZ'
        
    nrf = rf.split('Z')
    
    minn = 10**10
    
    for x in range(len(nrf) - 119):
        a = len('Z' + 'Z'.join(nrf[x:x+119]) + 'Z')
        minn = min(a, minn)
        
    print(minn)
    

# f()