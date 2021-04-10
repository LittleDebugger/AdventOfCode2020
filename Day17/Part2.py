from collections import defaultdict

file = [l.strip() for l in open("c:\\aoc\\2020\\Day17.txt")]

nodes = defaultdict(lambda: 0)

y = 0
z = 0
for line in file:
    for i, c in enumerate(line):
        if c == '#':
            nodes[(i, y, z, 0)] = 1
    y += 1

minX = -1
maxX = len(line) + 1
minY = -1
maxY = len(file) + 1
minZ = -1
maxZ = 1
minW = -1
maxW = 1


def getAdjCount(co):
    count = 0
    for x in range(co[0] - 1, co[0] + 2):
        for y in range(co[1] - 1, co[1] + 2):
            for z in range(co[2] - 1, co[2] + 2):
                for w in range(co[3] - 1, co[3] + 2):
                    if x == co[0] and y == co[1] and z == co[2] and w == co[3]:
                        continue
                    nn = (x, y, z, w)
                    if nodes[nn] == 1:
                        count += 1
    return count


i = 0

while i < 6:
    copy = defaultdict(lambda: 0)

    t = 0
    for n in copy.keys():
        if copy[n] == 1:
            t += 1

    for xx in range(minX - 1, maxX + 2):
        for yy in range(minY - 1, maxY + 2):
            for zz in range(minZ - 1, maxZ + 2):
                for ww in range(minW - 1, maxW + 2):
                    node = (xx, yy, zz, ww)
                    adj = getAdjCount(node)
                    if nodes[node] == 1 and adj in [2, 3]:
                        copy[node] = 1
                    elif nodes[node] == 0 and adj == 3:
                        copy[node] = 1

    nodes = defaultdict(lambda: 0)

    for e in copy.keys():
        nodes[e] = copy[e]

    t = 0
    for n in nodes.keys():
        if nodes[n] == 1:
            t += 1

    minX -= 1
    minY -= 1
    minZ -= 1
    minW -= 1
    maxX += 1
    maxY += 1
    maxZ += 1
    maxW += 1

    i += 1

    print('total: ', t)
