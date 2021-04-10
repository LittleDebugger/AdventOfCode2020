import re

file = [l.strip() for l in open("c:\\aoc\\2020\\Day16.txt")]

valid = []

section = 0
for l in file:
    if not l:
        break
    if section == 0:
        s = re.split(' |:|-', l)
        for t in range(int(s[-2]), int(s[-1]) + 1):
            valid.append(t)
        for t in range(int(s[-5]), int(s[-4]) + 1):
            valid.append(t)

myTicket = ''
quit = False
for l in file:
    myTicket = l
    if quit:
        break
    if l == 'your ticket:':
        quit = True

others = []
quit = False
for l in file:
    if quit:
        others.append(l)
    if l == 'nearby tickets:':
        quit = True

invalid = 0
for o in others:
    for t in [int(t) for t in o.split(',')]:
        if t not in valid:
            invalid += t

print(invalid)
