file = open('input.txt')
inp = file.readlines()
file.close()


start = [u for u, x in enumerate(inp) if x.find('S') > 0]
start.append(inp[start[0]].find('S'))

end = [u for u, x in enumerate(inp) if x.find('E') > 0]
end.append(inp[end[0]].find('E'))

map = [[0 for x in range(len(inp[0]))] for y in range(len(inp)-1)]
map[start[0]][start[1]] = 1

dirs = [[0,1], [1,0], [0,-1], [-1,0]]
d = 1

here = start
i = 2
while here != end:
    for j in [-1, 0, 1]:
        next = [here[0] + dirs[(d+j)%4][0], here[1] + dirs[(d+j)%4][1]]
        if inp[next[0]][next[1]] == '.' or inp[next[0]][next[1]] == 'E':
            d = (d+j)%4
            map[next[0]][next[1]] = i
            here = next.copy()
            i += 1

out = 0
for i in range(1,len(inp)-1):
    for j in range(1,len(inp[0])-1):
        if inp[i][j] == '#':
            if (inp[i+1][j] in ['S', 'E', '.'] and
                inp[i-1][j] in ['S', 'E', '.'] and
                abs(map[i+1][j] - map[i-1][j]) > 101):
                out += 1
            elif (inp[i][j+1] in ['S', 'E', '.'] and
                  inp[i][j-1] in ['S', 'E', '.'] and
                  abs(map[i][j+1] - map[i][j-1]) > 101):
                out += 1
print(out) 


# part two

here = start
d = 1
out = 0
while here != end:
    combos = []
    for u in range(max([0, here[0]-20]), min([len(inp), here[0]+21])):
        for v in [here[1] + x for x in range(-20, 21) if 
                  abs(x) + abs(u-here[0]) <= 20 and 0 < here[1] + x < len(inp[0])-2]:
            dist = abs(u-here[0]) + abs(v-here[1])
            if inp[u][v] in ['.', 'E'] and map[u][v] - map[here[0]][here[1]] - dist > 99:
                out += 1

    for j in [-1, 0, 1]:
        next = [here[0] + dirs[(d+j)%4][0], here[1] + dirs[(d+j)%4][1]]
        if inp[next[0]][next[1]] == '.' or inp[next[0]][next[1]] == 'E':
            d = (d+j)%4
            here = next.copy()
            break
print(out)