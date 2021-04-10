from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day20.txt")]

names = []
grids = []
starts = []


def getEdge(gg, r):
    r = r - 1
    return rotate(gg, r, False)[0]


def rotate(gg, r, f):
    r = 3 - r
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

print(s)


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

topLeft = rotate(starts[corner], r, False)
startI = corner
used = []


def getNext(i, peice, side):
    edge = getEdge(peice, side)
    print(edge)
    for other in links[i]:
        if other in used:
            continue
        for f in range(0, 2):
            otherOne = starts[other]
            for r in range(0, 4):
                good = True
                next = getEdge(otherOne, r)
                for i in range(0, len(edge)):
                    if edge[i] != next[i]:
                        good = False
                        break
                if good:
                    used.append(other)
                    return rotate(otherOne, side, False)
            otherOne = starts[other][::-1]
    print('fai')
    exit()
