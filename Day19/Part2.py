from collections import defaultdict as dd
from itertools import product

file = [l.strip() for l in open("c:\\aoc\\2020\\Day19.txt")]
print(file[0])

maxLength = 0
rulesSection = []
codes = set()

s = 0
for line in file:
    if not line:
        s = 1
    if s == 0:
        if line.startswith('8:'):
            line = '8: 42 | 42 8'
        if line.startswith('11:'):
            line = '11: 42 31 | 42 11 31'
        rulesSection.append(line)
    else:
        if len(line) > maxLength:
            maxLength = len(line)
        codes.add(line)

rules = dd(list)

for r in rulesSection:
    n = int(r.split(':')[0])
    rest = r.split(':')[1]
    rest = rest.split('|')
    for t in rest:
        rules[n].append([])
        for s in t.split(' '):
            if s:
                try:
                    rules[n][-1].append(int(s))
                except:
                    rules[n][-1] = s[1]


copyCodes = [yy for yy in codes]

allowed = set()

for loooo in range(0, 10):
    mem = dict()
    currentMax = 0
    maxD8 = loooo
    maxD11 = loooo

    def getNum(n, d8, d11, depth):
        global currentMax,  maxD8, maxD11
        if n in ['a', 'b']:
            return n
        if rules[n] in ['a', 'b']:
            return rules[n]

        if n in mem:
            return mem[n]

        returns = []
        groups = rules[n]

        if n == 8:
            d8 += 1
            if d8 > maxD8:
                groups = [groups[0]]
        if n == 11:
            d11 += 1
            if d11 > maxD11:
                groups = [groups[0]]

        for group in groups:
            nn = []
            for g in group:
                nn.append(getNum(g, d8, d11, depth + 1))

            t = [y for y in product(*nn)]
            for tt in t:
                word = ''.join(tt)

                for cccc in codes:
                    if word in cccc:
                        returns.append(word)
                        break
        mem[n] = returns

        return returns

    for zz in (getNum(0, 0, 0, 0)):
        allowed.add(zz)

    t = 0
    removes = []
    for c in copyCodes:
        if c in allowed:
            removes.append(c)
            t += 1

    for rrr in removes:
        try:
            codes.remove(rrr)
        except:
            pass

    print(t)
