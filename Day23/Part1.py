file = [l.strip() for l in open("c:\\aoc\\2020\\Day23.txt")]

input = '952316487'

cups = [int(a) for a in input]
maxN = max(cups)

pos = 0
cc = 1

while True and cc <= 100:
    cc += 1
    pickup = cups[pos + 1: pos + 4]
    start = 0
    next = (cups[pos] - 1) % maxN
    currentVal = cups[pos]

    if len(pickup) < 3:
        start += 3 - len(pickup)
        pickup += cups[0: 3 - len(pickup)]
    cups = cups[start:pos + 1] + cups[pos + 4:]

    i = pos

    c = len(cups)
    ok = False
    while True:
        for i in range(pos, c + pos):
            if cups[i % len(cups)] == next:
                ok = True
                break
        next -= 1
        if next == -1:
            next = maxN
        if ok:
            break
    des = i % len(cups)
    cups = cups[0:des + 1] + pickup + cups[des + 1:]

    for a in range(0, len(cups)):
        if cups[a] == currentVal:
            break
    pos = (a + 1) % len(cups)


for offset in range(0, len(cups)):
    if cups[offset] == 1:
        break

t = ''
for a in range(0, len(cups) - 1):
    t += str(cups[(a + offset + 1) % len(cups)])

print(t)
