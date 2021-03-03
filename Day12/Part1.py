file = [l.strip() for l in open("c:\\aoc\\2020\\Day12.txt")]
print(file[0])


class Direction:
    North = 0
    East = 1
    South = 2
    West = 3


d = Direction.East

x = 0
y = 0

for l in file:
    c = l[0]
    m = int(l[1:])
    print(c, m)
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
    elif c == 'F':
        if d == 0:
            y += m
        elif d == 1:
            x += m
        elif d == 2:
            y -= m
        elif d == 3:
            x -= m
        else:
            raise Exception('fail')
    else:
        raise Exception('fail')
print(abs(x) + abs(y))
