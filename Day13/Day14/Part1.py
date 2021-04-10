from collections import defaultdict
import re

file = [l.strip() for l in open("c:\\aoc\\2020\\Day14.txt")]

dd = defaultdict(lambda: 0)
for l in file:
    if l[0:4] == 'mask':
        mask = l[7:]
        continue
    word = re.split(' |\[|\]', l)
    reg = word[1]
    val = word[4]
    b = "{0:b}".format(int(val))
    newWord = ""
    for i in range(0, 36):
        c = 35 - i
        if mask[i] == 'X':
            if i - (36 - len(b)) >= 0:
                newWord = newWord + b[i - (36 - len(b))]
            else:
                newWord = newWord + "0"
        else:
            newWord = newWord + mask[i]

    dd[reg] = int(newWord, 2)

t = 0
for a in dd:
    t += dd[a]
print(t)
