
file = open('input.txt')
inp = file.readlines()
file.close()

rulez = 1176

orders = []
for i in range(rulez):
    orders.append([int(n) for n in inp[i].split('|')])

out = 0
for x in inp[rulez+1:]:
    upd = [int(n) for n in x.split(',')]
    flag = 1 
    for i in range(len(upd)):
        for j in range(i, len(upd)):
            for k in range(rulez):
                if orders[k][0] == upd[j] and orders[k][1] == upd[i]:
                    flag = 0
    if flag:
        out += upd[int(len(upd)/2)]

print(out)


# part 2

out = 0
for x in inp[rulez+1:]:
    upd = [int(n) for n in x.split(',')]
    flag = 1
    for i in range(len(upd)):
        for j in range(i, len(upd)):
            for k in range(rulez):
                if orders[k][0] == upd[j] and orders[k][1] == upd[i]:
                    flag = 0
    if not(flag):
        for i in range(1, len(upd)):
            for j in [i-l for l in range(i)]:
                for k in range(rulez):
                    if orders[k][0] == upd[j] and orders[k][1] == upd[j-1]:
                        upd[j-1], upd[j] = upd[j], upd[j-1]
        out += upd[int(len(upd)/2)]

print(out)