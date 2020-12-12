tt = 1

for xx, yy in [[1,1], [3,1], [5,1], [7, 1], [1, 2]]:
    file = [l.strip() for l in open("c:\\aoc\\2020\\Day3.txt")]
    y = 0
    x = 0
    t = 0

    while y < len(file):
        if file[y][x % len(file[y])] == '#':
            t += 1
        x += xx
        y += yy

    tt = tt * t

print (tt)




