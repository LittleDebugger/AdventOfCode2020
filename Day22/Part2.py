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


def recurse(cards, depth):

    had = []

    had.append(set())
    had.append(set())

    cardsT = [tuple(cards[0]), tuple(cards[1])]
    round = 1
    while True:
        round += 1
        had[0].add(cardsT[0])
        had[1].add(cardsT[1])

        player1Wins = False

        c1 = cards[0].pop(0)
        c2 = cards[1].pop(0)

        if len(cards[0]) >= c1 and len(cards[1]) >= c2:
            player1Wins = recurse([cards[0][:c1], cards[1][:c2]], depth + 1)
        else:
            player1Wins = c1 > c2
            if player1Wins:
                pass
            else:
                pass

        if player1Wins:

            cards[0].append(c1)
            cards[0].append(c2)
        else:
            cards[1].append(c2)
            cards[1].append(c1)

        if (len(cards[1]) == 0):
            return True
        if (len(cards[0]) == 0):
            t = 0
            return False

        cardsT = [tuple(cards[0]), tuple(cards[1])]

        if cardsT[0] in had[0]:
            return True
        if cardsT[1] in had[1]:
            return True


recurse(cards, 1)

if (len(cards[0]) > 0):
    printIt(cards[0])
else:
    printIt(cards[1])
