def task_5():
    for x in range(256):
        b = bin(x)[2:]
        if len(b) < 8:
            b = "0"*(8-len(b)) + b

        b = b.replace('1', '*')
        b = b.replace('0', '1')
        b = b.replace('*', '0')

        if int(b, 2) - x == 111:
            print(x)
