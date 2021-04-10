from collections import namedtuple as nt

input = '952316487'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


lookup = dict()

first = Node(int(input[0]))
lookup[first.value] = first
node = first

nodesCount = 1
for c in input[1:]:
    nodesCount += 1
    previous = node
    node = Node(int(c))
    lookup[node.value] = node
    previous.next = node


for a in range(nodesCount + 1, 1000000 + 1):
    nodesCount += 1
    previous = node
    node = Node(a)
    lookup[node.value] = node
    previous.next = node

node.next = first


def printIt(node):
    for i in range(0, nodesCount):
        print(node.value, end=' ')

        node = node.next
    print(node.value)


node = first

i = 0

while i < 10000000:
    i += 1
    pickupNode = node.next
    node.next = pickupNode.next.next.next
    pickupVals = [pickupNode.value,
                  pickupNode.next.value, pickupNode.next.next.value]

    ok = False
    destinationValue = node.value
    while not ok:
        ok = True
        destinationValue -= 1
        if destinationValue == 0:
            destinationValue = nodesCount
        if destinationValue in pickupVals:
            ok = False

    destinationNode = lookup[destinationValue]
    afterPickup = destinationNode.next
    destinationNode.next = pickupNode
    pickupNode.next.next.next = afterPickup

    node = node.next

print(lookup[1].next.value * lookup[1].next.next.value)
