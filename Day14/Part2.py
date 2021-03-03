from collections import defaultdict
from itertools import product
import re

bins = [0,1]

file = [l.strip() for l in open("c:\\aoc\\2020\\Day14.txt")]

dd = defaultdict(lambda:0)
for l in file:
    if l[0:4] == 'mask':
        mask = l[7:]
        continue
    word = re.split(' |\[|\]', l)
    reg = word[4]
    val = word[1]
    b = "{0:b}".format(int(val))
    newWord = ""
    xs = 0
    for i in range(0, 36):
        c = 35 - i
        if mask[i] == '0':
            if i - (36 - len(b)) >= 0:
                newWord = newWord + b[i - (36 - len(b))]
            else:
                newWord = newWord + "0"
        elif mask[i] == '1':
            newWord = newWord + '1'
        else:
            xs += 1
            newWord = newWord + 'X'

    times = [bins] * xs
    
    for y in [z for z in product(*times)]:
        print(y)
        wordCopy = newWord[:]
        for x in y:
            wordCopy = wordCopy.replace('X', str(x), 1)
        dd[int(wordCopy, 2)] = reg
t = 0
for a in dd:
    t += int(dd[a])
print(t)