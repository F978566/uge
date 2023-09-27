def task_25():
    a = [185_311, 185_330]

    count = 0
    d_count = []

    for x in range(a[0], a[1]+1):
        for i in range(1, x+1):
            if x % i == 0:
                # print(f'{x} {i}')
                d_count.append(i)
                count += 1
        if count == 4:
            print(*d_count)
            count = 0
            d_count = []
        else:
            count = 0
            d_count = []

task_25()