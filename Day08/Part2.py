file = [l.strip() for l in open("c:\\aoc\\2020\\Day8.txt")]

for xx in range(0, len(file)):
    file = [l.strip() for l in open("c:\\aoc\\2020\\Day8.txt")]
    if file[xx].startswith('jmp'):
        file[xx] = file[xx].replace('jmp', 'nop')
    elif file[xx].startswith('nop'):
        file[xx] = file[xx].replace('nop', 'jmp')

    x = 0
    g = 0
    oldX = x
    visited = []
    done = False
    c = 0
    while not done:
        c += 1
        if c > 1000000:
            break
        if x >= len(file):
            print(g)
            exit()
        com = file[x][0:3]

        oldX = x
        if com == 'nop':
            pass
        elif com == 'acc':
            g += int(file[x][3:])
        elif com == 'jmp':
            x += int(file[x][3:]) - 1

        x += 1

        if x in visited:
            break
        visited.append(x)
        oldX = x
