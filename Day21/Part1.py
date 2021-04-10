from collections import defaultdict as dd

allAls = set()
allIns = set()
alMaps = dd(list)
alToInMaps = dd(list)
possibles = dd(set)
appears = dd(lambda: 0)


file = [l.strip() for l in open("c:\\aoc\\2020\\Day21.txt")]

for line in file:
    i, a = line.split('(contains')
    a = a[0:-1]
    ins = i.split()
    als = a.replace(',', '').split()
    for a in als:
        alToInMaps[a].append(ins)
    for i in ins:
        appears[i] += 1
        allIns.add(i)
        for a in als:
            allAls.add(a)
            possibles[a].add(i)


for a in alToInMaps:
    removes = set()
    for al in possibles[a]:
        for aMaps in alToInMaps[a]:
            if al not in aMaps:
                removes.add(al)
    for r in removes:
        possibles[a].remove(r)


def go(mappedAls, mappedIns):
    if (len(mappedAls) == len(allAls)):
        t = 0
        for i in allIns:
            if i not in mappedIns:
                t += appears[i]
        print(t)
        exit()

    for al in allAls:
        if al in mappedAls:
            continue
        for ingredient in possibles[al]:
            if ingredient in mappedIns:
                continue

            mappedAlsCopy = mappedAls[:]
            mappedInsCopy = mappedIns[:]
            mappedAlsCopy.append(al)
            mappedInsCopy.append(ingredient)
            go(mappedAlsCopy, mappedInsCopy)


go([], [])
