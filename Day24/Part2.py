from collections import defaultdict

file = [l.strip() for l in open("c:\\aoc\\2020\\Day24.txt")]

d = defaultdict(lambda: False)

minX = 0
maxX = 0
minY = 0
maxY = 0
minsMax = [0, 0, 0, 0]


def setXy(x, y):
    global maxX, maxY, minX, minY
    if x > maxX:
        maxX = x + 1
    if x < minX:
        minX = x - 1
    if y > maxY:
        maxY = y + 1
    if y < minY:
        minY = y - 1


for line in file:
    x = 0
    y = 0
    line = line + ' '
    i = 0
    while i < len(line):
        if line[i:i+2] == 'se':
            x += 1
            y -= 1
            i += 1
        elif line[i:i + 2] == 'sw':
            #x -= 1
            y -= 1
            i += 1
        elif line[i:i + 2] == 'ne':
            #x += 1
            y += 1
            i += 1
        elif line[i:i + 2] == 'nw':
            x -= 1
            y += 1
            i += 1
        elif line[i] == 'e':
            x += 1
        elif line[i] == 'w':
            x -= 1
        elif not line or line[i] == ' ':
            pass
        else:
            exit()

        setXy(x, y)

        i += 1
    d[(x, y)] = not d[(x, y)]

t = 0
for a in d:
    if d[a]:
        t += 1

daysT = 100
for days in range(0, daysT):
    dCopy = defaultdict(lambda: False)
    for dd in d:
        dCopy[dd] = d[dd]

    total = 0
    for dd in dCopy:
        if dCopy[dd]:
            total += 1

    for y in range(minY - 5, maxY + 5):
        for x in range(minX - 5, maxX + 5):
            adj = 0
            if d[(x + 1, y)]:
                setXy(x + 1, y)
                adj += 1
            if d[(x - 1, y)]:
                setXy(x - 1, y)
                adj += 1
            if d[(x, y + 1)]:
                setXy(x, y + 1)
                adj += 1
            if d[(x, y - 1)]:
                setXy(x, y - 1)
                adj += 1

            if d[(x + 1, y - 1)]:
                setXy(x + 1, y - 1)
                adj += 1
            if d[(x - 1, y + 1)]:
                setXy(x - 1, y + 1)
                adj += 1

            if (d[(x, y)] and (adj == 0 or adj > 2)):
                dCopy[(x, y)] = False
            elif (not d[(x, y)] and (adj == 2)):
                dCopy[(x, y)] = True

    d = defaultdict(lambda: False)

    for dd in dCopy:
        d[dd] = dCopy[dd]

total = 0
for dd in dCopy:
    if dCopy[dd]:
        total += 1

print(total)
