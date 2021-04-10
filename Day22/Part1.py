file = [l.strip() for l in open("c:\\aoc\\2020\\Day22.txt")]

p = -1
cards = []
for line in file:
    if line.startswith('Player'):
        p += 1
        cards.append([])
    elif line:
        cards[-1].append(int(line))


def printIt(win):
    t = 0
    for i, a in enumerate(win):
        next = a * (len(win) - (i))
        t += next
    print(t)


while True:
    if (len(cards[1]) == 0):
        printIt(cards[0])
        exit()
    if (len(cards[0]) == 0):
        t = 0
        printIt(cards[1])
        exit()

    c1 = cards[0].pop(0)
    c2 = cards[1].pop(0)

    if c1 > c2:
        cards[0].append(c1)
        cards[0].append(c2)
    else:
        cards[1].append(c2)
        cards[1].append(c1)
