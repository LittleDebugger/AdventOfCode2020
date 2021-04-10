from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day7.txt")]

innerOuter = dd(list)
outerInner = dd(lambda: dd(list))

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
        outerInner[carries][carrier] = n

canCarry = set()
bag = ['shiny gold']
while len(bag) > 0:
    for c in outerInner[bag.pop(0)]:
        canCarry.add(c)
        bag.append(c)

print(len(canCarry))
