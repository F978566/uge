"""
    (№ 6526) Текстовый файл 24-259.txt состоит не более чем из 106 символов и содержит
    только символы A, T, G, C. Найдите длину наибольшей цепочки символов, которая начинается
    с ATG, заканчивается на TAA и между этими группами символов не содержит цепочек TAA, TGA и TAG.
"""

def f():
    with open('f.txt', 'r') as f:
        rf = f.readline()

    i = 0
    current_length = 0

    maxx = 0

    while i < len(rf):
        if rf[i:i+3] == 'ATG':
            i += 3
            current_length = 3

            while i < len(rf):
                if rf[i:i+3] in ['TAA', 'TGA', 'TAG']:
                    break
                
                current_length += 1
                i += 1

            maxx = max(current_length, maxx)
        else:
            i += 1

    print(maxx)


f()