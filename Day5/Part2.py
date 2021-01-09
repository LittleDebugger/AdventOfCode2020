#from collections import Counter
#from collections import namedtuple as nt
#from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day5.txt")]
print(file[0])

seats = {}

mm = 0
for l in file:
    r = l[0:7]
    c = l[7:]

    min = 0
    max = 127
    diff = 64
    for letter in r:
        if (letter == 'B'):
            min += diff
        else:
            max -= diff
        diff //= 2

    row = max
    min = 0
    max = 7
    diff = 4
    for letter in c:
        if (letter == 'R'):
            min += diff
        else:
            max -= diff
        diff //= 2

    col = max
    id = row * 8 + col
    if id > mm:
        mm = id
 #   print(row, col, id)
    seats[id] = True
#print (mm)

for a in range(0, 900):
    if a not in seats:
        print(a)


