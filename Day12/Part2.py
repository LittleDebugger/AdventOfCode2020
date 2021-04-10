file = [l.strip() for l in open("c:\\aoc\\2020\\Day12.txt")]
print(file[0])


class Direction:
    North = 0
    East = 1
    South = 2
    West = 3


x = 10
y = 1
xx = 0
yy = 0

for l in file:
    d = 0
    c = l[0]
    m = int(l[1:])
    if c == 'N':
        y += m
    elif c == 'S':
        y -= m
    elif c == 'E':
        x += m
    elif c == 'W':
        x -= m
    elif c in 'LR':
        if c == 'L':
            m //= 90
            d = ((d - m) + (4 * 100)) % 4
        elif c == 'R':
            m //= 90
            d = ((d + m) + (4 * 100)) % 4
        if d == 0:
            pass
        if d == 1:
            p = x
            x = y
            y = -p
        if d == 2:
            y = -y
            x = -x
        if d == 3:
            p = x
            x = -y
            y = p
    elif c == 'F':
        xo = x * m
        xx += xo
        yo = y * m
        yy += yo
    else:
        raise Exception('fail')
    print(x, y, xx, yy, abs(xx) + abs(yy))
print(abs(xx) + abs(yy))
