import itertools

def task():
    al = '01234567'

    word = itertools.permutations(al, 5)
    words = list(word)

    c = 0

    for x in words:
        flag = True
        for i in range(4):
            if (x[0] == '0') or (int(x[i]) % 2 == 0 and int(x[i+1]) % 2 == 0) or (int(x[i]) % 2 != 0 and int(x[i+1]) % 2 != 0):
                flag = False
        if flag:
            c += 1
    
    print(c)

task()
