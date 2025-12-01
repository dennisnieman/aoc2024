with open('input.txt') as file:
    inp = file.read().splitlines() 


computers = []
for i in inp:
    one = i[:2]
    if not(one in computers):
        computers.append(one)
    two = i[3:]
    if not(two in computers):
        computers.append(two)

n = len(computers)
conn = array([[0 for x in range(n)] for y in range(n)])
for i in inp:
    one, two = i[:2], i[3:]
    onePos, twoPos = computers.index(one), computers.index(two)
    conn[onePos][twoPos] = 1
    conn[twoPos][onePos] = 1

triples = []
for i in range(n):
    for j in range(i+1, n):
        if conn[i, j] == 1:
            for k in range(1, n):
                if k != i and conn[k, j] == 1 and conn[k, i] == 1:
                    if not(sorted([i, j, k]) in triples):
                        triples.append(sorted([i, j, k]))

print(sum(any(computers[i][0] == 't' for i in t) for t in triples))


# part 2

hist = []
largestGroup = []
def expand(gr):
    # recursively expand group gr with connected computers
    # to determine the largest group containing gr
    global hist, largestGroup
    if gr in hist:
        return
    hist.append(gr)
    flag = 0
    for j in range(n):
        if all(conn[j, k] for k in gr) and not(j in gr):
            flag = 1
            expand(sorted(gr + [j]))
    if not(flag) and len(gr) > len(largestGroup):
        largestGroup = gr

largestGroups = []
seen = []
for i in range(n):
    if not(i in seen):
        largestGroup = []
        expand([i])
        for l in largestGroup:
            seen.append(l)
        largestGroups.append(largestGroup)

sizes = array([len(g) for g in largestGroups])
party = largestGroups[sizes.argmax()]

print(','.join(sorted([computers[p] for p in party])))