from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day7.txt")]

innerOuter = dd(list)
outerInner = dd(lambda: dd(lambda: 0))

for s in file:
    ss = s.split(' ')
    carrier = ss[0] + ' ' + ss[1]
    ss = ' '.join(ss[4:])
    ss = ss[:-1]
    ss = ss.split(', ')

    for sp in ss:
        if sp == 'no other bags':
            continue
        spp = sp.split(' ')
        carries = spp[1] + ' ' + spp[2]
        n = int(spp[0])
        outerInner[carrier][carries] = n

canCarry = []
bag = [('shiny gold', 1)]
while len(bag) > 0:
    current = bag.pop(0)
    for c in outerInner[current[0]]:
        canCarry.append((c, current[1] * outerInner[current[0]][c]))
        bag.append((c, current[1] * outerInner[current[0]][c]))

t = 0
for i in canCarry:
    t += i[1]

print(t)
