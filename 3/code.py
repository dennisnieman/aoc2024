
out = 0
for i in inp:
    i0 = 0
    i1 = 0
    while(i0 > -1):
        i0 = i.find('mul(', i0+1)
        i1 = i.find(')', i0)
        toMult = i[i0+4:i1].split(',')
        if i0 > -1 and len(toMult)==2 and toMult[0].isdigit() and toMult[1].isdigit():
            out += int(toMult[0]) * int(toMult[1])
print(out)

# part 2
out = 0
i = ''.join(inp)        # merge all lines into one big line
chop = i.split("do()")
relev = ''
for c in chop:
    j = c.find("don't()")
    if j == -1:
        relev += c
    else:
        relev += c[:j]
i0 = 0
i1 = 0
while(i0 > -1):
    i0 = relev.find('mul(', i0+1)
    i1 = relev.find(')', i0)
    toMult = relev[i0+4:i1].split(',')
    if i0 > -1 and len(toMult)==2 and toMult[0].isdigit() and toMult[1].isdigit():
        out += int(toMult[0]) * int(toMult[1])
print(out)





