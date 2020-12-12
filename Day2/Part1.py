file = [line.strip() for line in open("c:\\aoc\\2020\\Day2.txt")]

t = 0
for l in file:
    b = l.split(' ')
    m = b[0].split('-')
    letter = b[1][0]
    word = b[2]
    count = word.count(letter)
    if int(m[0]) <= count <= int(m[1]):
        t += 1
print(t)
