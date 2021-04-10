from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day20.txt")]

names = []
grids = []
starts = []


def getEdge(gg, r):
    return rotate(gg, r, False)[0]


def rotate(gg, r, f):
    r = 4 - r
    if f:
        r += 2
    ggg = gg[:]

    if f:
        ggg = ggg[::-1]

    for i in range(0, r):
        t = []
        for x in range(0, len(ggg)):
            t.append([])
            for y in range(0, len(ggg)):
                t[-1].append(ggg[len(ggg) - y - 1][x])
        ggg = t
    return ggg


x = -1
for line in file:
    if not line:
        continue
    if line.startswith('Tile'):
        x += 1
        if x > 0:
            starts.append(grids[-1])
        grids.append([])
        names.append(line.split(' ')[1])
        continue
    cs = [c for c in line]
    grids[-1].append(cs)

edges = dd(list)
allEdges = []
starts.append(grids[-1])

for i, g in enumerate(grids):
    grid = g

    for y in range(0, 2):
        start = grid[:]

        for r in range(0, 4):
            grid = rotate(start, r, y == 1)
            edges[i].append(grid[0])

s = 1
cornersP = []
edgesP = []
restP = []
links = dd(set)

for g in edges:
    thisGrid = edges[g]
    cc = 0

    match = 0
    for gg in edges:
        if g == gg:
            continue
        other = edges[gg]
        for r in thisGrid:
            for rr in other:
                got = True
                for i in range(0, len(r)):
                    if r[i] != rr[i]:
                        got = False
                if got:
                    links[g].add(gg)
                    links[gg].add(g)
                    match += 1
    if match == 4:
        s *= int(names[g][0:-1])
        cornersP.append(g)
    if match == 6:
        edgesP.append(g)
    if match == 8:
        restP.append(g)


def compare(i, rot, f):
    e = rotate(starts[i], rot, f)[0]
    match = 0
    for gg in edges:
        other = edges[gg]

        for rr in other:
            got = True

            for i in range(0, len(e)):
                if e[i] != rr[i]:
                    got = False
            if got:
                match += 1
    return match - 1


corner = cornersP[0]
for r in range(0, 4):
    if compare(corner, r, False) == 1 and compare(corner, r + 1, False):
        break

topLeft = rotate(starts[corner], r + 2, True)

startI = corner
used = []


def getNext(i, peice, side):
    edge = getEdge(peice, side)
    for other in links[i]:
        if other in used:
            continue
        otherOne = starts[other]
        for f in range(0, 2):

            for r in range(0, 4):
                good = True
                next = getEdge(otherOne, r)
                for i in range(0, len(edge)):
                    if edge[i] != next[i]:
                        good = False
                        break
                if good:
                    used.append(other)
                    if side == 1:
                        otherOne = otherOne[::-1]
                        return other, rotate(otherOne, 3 - r, False)
                    else:
                        # exit()
                        return other, rotate(otherOne, 4 - r, True)
            otherOne = otherOne[::-1]
    print('fail')
    exit()


next = topLeft
i = startI

width = ((len(cornersP) + len(edgesP)) // 4) + 1

fin = []
fin.append(names[i])

newGrid = []
for a in range(0, width):
    newGrid.append([])
    for b in range(0, width):
        newGrid[-1].append('!')

startOfline = next[:]
startOfLineI = i

newGrid[0][0] = startOfline
for y in range(width):

    for x in range(1, width):
        i, next = (getNext(i, next, 1))
        fin.append(names[i])
        newGrid[y][x] = next

    if y == width - 1:
        break
    i, next = (getNext(startOfLineI, startOfline, 2))

    fin.append(names[i])
    startOfline = next
    startOfLineI = i

    newGrid[y + 1][0] = next

newWidth = (len(starts[0][0]) - 2)

done = []
for y in range(0, width * newWidth):
    done.append([])
    for x in range(0, width * newWidth):
        done[-1].append(newGrid[y // newWidth][x // newWidth]
                        [(y % newWidth) + 1][(x % newWidth) + 1])

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "]

t = 0
cou = 0
while t == 0:
    cou += 1
    found = 0
    done = rotate(done, 1, cou == 5)

    for y in range(0, len(done) - len(monster)):
        for x in range(0, len(done[0]) - len(monster[0])):
            mo = True
            for yy in range(0, len(monster)):
                for xx in range(0, len(monster[0])):
                    if monster[yy][xx] == '#' and done[y + yy][x + xx] != '#':
                        mo = False
            if mo:
                found = 1
                for yy in range(0, len(monster)):
                    for xx in range(0, len(monster[0])):
                        if monster[yy][xx] == '#':
                            done[y + yy][x + xx] = '!'

    if found == 0:
        continue

    for y in range(0, len(done)):
        for x in range(0, len(done[y])):
            if done[y][x] == '#':
                t += 1

    print(t)
