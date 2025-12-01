with open('input.txt') as file:
    inp = file.read().splitlines() 



def dirs(pos, target, pad):
    dirList = [[pos[0], pos[1], '']]
    while dirList[0][0] != target[0] or dirList[0][1] != target[1]:
        dirListNew = []
        for d in dirList:
            if d[0] < target[0] and pad[d[0]+1][d[1]] != 'x':
                dirListNew.append([d[0]+1, d[1], d[2]+'v'])
            elif d[0] > target[0] and pad[d[0]-1][d[1]] != 'x':
                dirListNew.append([d[0]-1, d[1], d[2]+'^'])
            if d[1] < target[1] and pad[d[0]][d[1]+1] != 'x':
                dirListNew.append([d[0], d[1]+1, d[2]+'>'])
            elif d[1] > target[1] and pad[d[0]][d[1]-1] != 'x':
                dirListNew.append([d[0], d[1]-1, d[2]+'<'])
        dirList = dirListNew.copy()
    return [d[2] for d in dirList]

botpad = ['x^A', 
          '<v>']

keypad = ['789',
          '456',
          '123',
          'x0A']

ins = []
outs = []
def instrLength(code, depth):
    # takes a code with one A at the end and computes length of shortest instruction
    if depth == maxDepth:
        return len(code)
    
    if (code, depth) in ins:
        return outs[ins.index((code, depth))]
    
    if depth == 0:
        pad, pos = keypad, [3, 2]
    else:
        pad, pos = botpad, [0, 2]

    length = 0
    for n in code:
        target = [[u, x.find(n)] for u, x in enumerate(pad) if x.find(n) > -1][0]
        length += min([instrLength(d+'A', depth+1) for d in dirs(pos, target, pad)])
        pos = target
    ins.append((code, depth))
    outs.append(length)
    return(length)

maxDepth = 26 # or 3 for part 1
ans = 0
for i in inp:
    ins = []
    outs = []
    ans += instrLength(i, 0) * int(i[:3])
print(ans)