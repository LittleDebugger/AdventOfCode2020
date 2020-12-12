file = [l.strip() for l in open("c:\\aoc\\2020\\Day4.txt")]

required = ['byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid']

t = 0
person = []
for l in file:
    if len(l) == 0:
        person = []
        continue
    for ll in l.split(' '):
        word = ll[:3]
        if word in required and word not in person:
            person.append(word)
    if len(person) >= len(required):
        person = []
        t += 1
print(t)
