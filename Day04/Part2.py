file = [l.strip() for l in open("c:\\aoc\\2020\\Day4.txt")]

required = ['byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid']

dig = dict()
dig['byr'] = [1920, 2002]
dig['iyr'] = [2010, 2020]
dig['eyr'] = [2020, 2030]

t = 0
person = []
for l in file:
    if len(l) == 0:
        person = []
        continue
    for ll in l.split(' '):
        word = ll[:3]
        val = ll[4:]
        if word in required and word not in person:
            fail = False
            if word in ['byr', 'iyr', 'eyr']:
                try:
                    if not (dig[word][0] <= int(val) <= dig[word][1]) or len(val) != 4:
                        fail = True
                except:
                    print(word, val, 'except')
                    fail = True
                    pass
            if word == 'hgt':
                try:
                    m = val[-2:]
                    if m not in ['cm', 'in']:
                        fail = True
                    h = val[:-2]
                    if m == 'cm':
                        if not (150 <= int(h) <= 193):
                            fail = True
                    elif m == 'in':
                        if not (59 <= int(h) <= 76):
                            fail = True
                except:
                    print(word, val)
                    fail = True
            if word == 'hcl':
                if len(val) != 7 or val[0] != '#':
                    fail = True
                elif not val[1:].isalnum():
                    fail = True
            if word == 'ecl' and val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                fail = True
            if word == 'pid':
                if len(val) != 9 or not val.isnumeric():
                    fail = True

            if fail:
                person = []
            else:
                person.append(word)
            if len(person) >= len(required):
                person = []
                t += 1
print(t)
