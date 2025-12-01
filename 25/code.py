with open('input.txt') as file:
    inp = file.read().splitlines() 

locks = []
keys = []

len(inp) # 3999
         # since 4000/8 = 500 and 8 is the height
         # of key/lock (7) plus space (1), there
         # are 500 keys+locks and 499 spaces

for i in range(500):
    block = inp[8*i : 8*i + 6]
    if block[0] == '#####':
        keys.append([sum(block[x][y]=='#' for x in range(1,6)) for y in range(5)])
    elif block[0] == '.....':
        locks.append([sum(block[x][y]=='#' for x in range(1,6)) for y in range(5)])

out = 0
for key in keys:
    for lock in locks:
        out += all(key[y] + lock[y] <= 5 for y in range(5))
print(out)


