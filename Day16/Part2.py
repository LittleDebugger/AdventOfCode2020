import re

file = [l.strip() for l in open("c:\\aoc\\2020\\Day16.txt")]

fields = []
allFields = []

section = 0
for l in file:
    if not l:
        break
    if section == 0:
        s = re.split(' |:|-', l)

        thisV = []
        for t in range(int(s[-2]), int(s[-1]) + 1):
            thisV.append(t)
            allFields.append(t)
        for t in range(int(s[-5]), int(s[-4]) + 1):
            thisV.append(t)
            allFields.append(t)
        fields.append(thisV)

myTicket = ''
quit = False
for l in file:
    myTicket = l
    if quit:
        break
    if l == 'your ticket:':
        quit = True

others = []
quit = False
for l in file:
    if quit:
        others.append(l)
    if l == 'nearby tickets:':
        quit = True

invalid = 0
good = []

for o in others:
    valid = True
    for m in [int(t) for t in o.split(',')]:
        if m not in allFields:
            valid = False
            break
    if valid:
        good.append(o)

good.append(myTicket)
goods = [[int(y) for y in t.split(',')] for t in good]

needs = [0, 1, 2, 3, 4, 5]

myGoods = [int(t) for t in myTicket.split(',')]
possibles = []

for field in fields:
    possibles.append([])
    for col in range(0, len(goods[0])):
        ok = True
        for person in goods:
            if person[col] not in field:
                ok = False
                break
        if ok:
            possibles[-1].append(col)

t = sum([len(a) for a in possibles])
oldT = 0

while t != oldT:
    oldT = t
    for a in possibles:
        if len(a) == 1:
            c = a[0]
            for i, b in enumerate(possibles):
                if c in b:
                    b.remove(c)
            a.append(c)
    t = sum([len(a) for a in possibles])

ans = 1
for i in range(0, 20):
    if i in needs:
        nextAns = myGoods[possibles[i][0]]
        ans *= nextAns

print(ans)
