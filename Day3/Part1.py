#from collections import Counter
#from collections import namedtuple as nt
#from collections import defaultdict as dd
import re # regex

file = [l.strip() for l in open("c:\\aoc\\2020\\Day3.txt")]
#print(file[0])

y = 0
x = 0
t = 0

while y < len(file):
    x += 3
    y += 1
    try:
        if file[y][x % len(file[y])] == '#':
            t += 1
    except:
        pass

print(t)



