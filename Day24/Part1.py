#from collections import Counter
#from collections import namedtuple as nt
from collections import defaultdict

file = [l.strip() for l in open("c:\\aoc\\2020\\Day24.txt")]
# print(file[0])

# e, se, sw, w, nw, and ne

d = defaultdict(lambda: False)

for line in file:
    x = 0
    y = 0
    line = line + ' '
    i = 0
    while i < len(line):
        print(i)
        print((x, y))
        print(print(line[i:i + 2]))
        # print(line[i:i+2])
        if line[i:i+2] == 'se':
            #x += 1
            y -= 1
            i += 1
        elif line[i:i + 2] == 'sw':
            x -= 1
            y -= 1
            i += 1
        elif line[i:i + 2] == 'ne':
            #x += 1
            y += 1
            i += 1
        elif line[i:i + 2] == 'nw':
            x -= 1
            y += 1
            i += 1
        elif line[i] == 'e':
            x += 1
        elif line[i] == 'w':
            x -= 1
        elif not line or line[i] == ' ':
            pass
        else:
            exit()

        i += 1
    print(line)
    print((x, y))
    d[(x, y)] = not d[(x, y)]

t = 0
for a in d:
    if d[a]:
        t += 1

print(t)
