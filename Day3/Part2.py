#from collections import Counter
#from collections import namedtuple as nt
#from collections import defaultdict as dd
import re # regex

tt = 1

for xx, yy in [[1,1], [3,1], [5,1], [7, 1], [1, 2]]:
    file = [l.strip() for l in open("c:\\aoc\\2020\\Day3.txt")]
    y = 0
    x = 0
    t = 0

    while y < len(file):
        x += xx
        y += yy
        try:
            if file[y][x % len(file[y])] == '#':
                t += 1
        except:
            pass
    print(t)
    tt = tt * t

print (tt)



