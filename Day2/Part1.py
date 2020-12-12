#from collections import Counter
#from collections import namedtuple as nt
#from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day2.txt")]
print(file[0])

t = 0
for l in file:
    b = l.split(' ')
    m = b[0].split('-')
    letter = b[1][0]
    word = b[2]
    count = word.count(letter)
    if count >= int(m[0]) and count <= int(m[1]):
        t += 1
print(t)