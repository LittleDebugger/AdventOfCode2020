file = [l.strip() for l in open("c:\\aoc\\2020\\Day8.txt")]

x = 0
g = 0
oldX = x
visited = []

while x <= len(file):
    print(file[x], g)
    com = file[x][0:3]

    oldX = x
    if com == 'nop':
        pass
    if com == 'acc':
        g += int(file[x][3:])
    if com == 'jmp':
        x += int(file[x][3:]) - 1

    x += 1
    x = x % len(file)

    if x in visited:
        print(g)
        exit()
    visited.append(x)
    oldX = x
