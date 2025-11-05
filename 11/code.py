from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/11')

file = open('input.txt')
inp = file.readlines()
file.close()

stones = inp[0].split()

for i in range(25):
    splits = 0
    for j in range(len(stones)):
        if int(stones[j+splits]) == 0:
            stones[j+splits] = '1'
        else:
            l = len(stones[j+splits])
            if l%2 == 0:
                left = str(int(stones[j+splits][:int(l/2)]))
                right = str(int(stones[j+splits][int(l/2):]))
                stones[j+splits] = left
                stones.insert(j+splits+1, right)
                splits += 1
            else:
                stones[j+splits] = str(2024 * int(stones[j+splits]))

print(len(stones))



# part 2


stones = sorted([[int(x), 1] for x in inp[0].split()])

for i in range(75):
    newStones = []
    for j in range(len(stones)):
        amount = stones[j][1]
        if stones[j][0] == 0:
            newStones.append([1, amount])
        else:
            stone = str(stones[j][0])
            l = len(stone)
            if l%2 == 0:
                left = int(stone[:int(l/2)])
                newStones.append([left, amount])
                right = int(stone[int(l/2):])
                newStones.append([right, amount])
            else:
                newStones.append([2024 * int(stone), amount])
    newStones.sort()
    stones = []
    j = 0
    while j < len(newStones):
        stone = newStones[j][0]
        k = max(u for u, x in enumerate(newStones) if x[0] == stone)
        if k > j:
            amount = sum(newStones[l][1] for l in range(j, k+1))
        else:
            amount = newStones[j][1]
        stones.append([stone, amount])
        j = k+1

print(sum(s[1] for s in stones))