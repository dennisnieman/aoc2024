from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/19')

file = open('input.txt')
inp = file.readlines()
file.close()

towels = inp[0][:-1].split(', ')

out = []

for j in range(len(inp[2:])):
    pattern = inp[j+2]
    if pattern[-1] == '\n': pattern = pattern[:-1]
    lookNext = [0]
    hist = [0]
    while len(lookNext) > 0:
        look = lookNext.copy()
        lookNext = []
        flag = 0
        for n in look:
            for t in towels:
                if pattern[n:n+len(t)] == t:
                    if n+len(t) == len(pattern):
                        out.append(j+2)
                        flag = 1
                    elif not(n + len(t) in hist):
                        hist.append(n + len(t))
                        lookNext.append(n + len(t))
            if flag: break
        if flag: break

print(len(out))



# part two


def count(i):
    global optionsCount
    if i == len(pattern):
        return 1
    elif optionsCount[i] > -1:
        return optionsCount[i]
    else:
        outSum = 0
        for t in towels:
            if pattern[i:i+len(t)] == t:
                outSum += count(i+len(t))
        optionsCount[i] = outSum
        return outSum

out2 = 0

for j in out:
    pattern = inp[j]
    if pattern[-1] == '\n': pattern = pattern[:-1]
    optionsCount = [-1 for j in range(len(pattern))]
    out2 += count(0)

print(out2)

