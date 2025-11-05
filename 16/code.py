from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/16')

file = open('input.txt')
inp = file.readlines()
file.close()

dirs = [[0,1], [1,0], [0,-1], [-1, 0]]

minScore = 1e7

seen = [[[minScore for i in range(4)] for j in range(len(inp))] for k in range(len(inp))]
here = [(139, 1, 0, 0)]

while len(here) > 0 :
    next = []
    for h in here:
        d = h[2]
        for n in [(h[0] + dirs[d][0], h[1] + dirs[d][1], d, h[3]+1),
                  (h[0] + dirs[(d+1)%4][0], h[1] + dirs[(d+1)%4][1], (d+1)%4, h[3]+1001),
                  (h[0] + dirs[(d+2)%4][0], h[1] + dirs[(d+2)%4][1], (d+2)%4, h[3]+2001),
                  (h[0] + dirs[(d+3)%4][0], h[1] + dirs[(d+3)%4][1], (d+3)%4, h[3]+1001)]:
            if inp[n[0]][n[1]] == '.' and n[3] < seen[n[0]][n[1]][n[2]]:
                seen[n[0]][n[1]][n[2]] = n[3]
                next.append(n)
            if inp[n[0]][n[1]] == 'E' and n[3] < minScore:
                minScore = n[3]
    here = next.copy()
print(minScore)


# part two

routes = [[(139, 1, 0, 0)]]

while len(routes) > 0 :
    next = []
    for r in routes:
        h = r[-1]
        d = h[2]
        for n in [(h[0] + dirs[d][0], h[1] + dirs[d][1], d, h[3]+1),
                  (h[0] + dirs[(d+1)%4][0], h[1] + dirs[(d+1)%4][1], (d+1)%4, h[3]+1001),
                  (h[0] + dirs[(d+2)%4][0], h[1] + dirs[(d+2)%4][1], (d+2)%4, h[3]+2001),
                  (h[0] + dirs[(d+3)%4][0], h[1] + dirs[(d+3)%4][1], (d+3)%4, h[3]+1001)]:
            if inp[n[0]][n[1]] == '.' and n[3] == seen[n[0]][n[1]][n[2]]:
                next.append(r + [n])
            if inp[n[0]][n[1]] == 'E' and n[3] == minScore:
                for c in r:
                    seen[c[0]][c[1]][c[2]] = 0
    routes = next.copy()

print(1 + sum(sum(any(x == 0 for x in seen[i][j]) for j in range(len(inp))) for i in range(len(inp))))
