def task_24():
    with open('24.txt', 'r') as f:
        rf = f.read()

    m = []
    count = 1

    for x in range(len(rf)):
        if not((rf[x] == 'a' and rf[x+1] == 'd') or (rf[x] == 'd' and rf[x+1] == 'a')):
            count += 1
        else:
            m.append(count)
            count = 1
    
    return max(m)


if __name__ == '__main__':
    print(task_24())