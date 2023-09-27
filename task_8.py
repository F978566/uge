def task_8():
    word = '12345'
    w = ''

    count = 0

    for a in word:
        for a1 in word:
            for a2 in word:
                for a3 in word:
                    for a4 in word:
                        w = a + a1 + a2 + a3 + a4
                        if w.count('1') == 3:
                            count += 1

    print(count)

if __name__ == '__main__':
    task_8()