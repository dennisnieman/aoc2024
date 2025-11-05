from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/14')

file = open('input.txt')
inp = file.readlines()
file.close()

from numpy import array, zeros

robots = zeros([101, 103])

for i in inp:
    vpos = i.find('v')
    init = array([int(x) for x in i[2:vpos-1].split(',')])
    velo = array([int(x) for x in i[vpos+2:].split(',')])
    final = (init + 100*velo) % array([101, 103])
    robots[final[0]][final[1]] += 1

print(sum(sum(robots[:50, :51])) * sum(sum(robots[:50, 52:])) * 
      sum(sum(robots[51:, :51])) * sum(sum(robots[51:, 52:])))


# part two 

for j in range(10000):
    robots = zeros([101, 103])
    for i in inp:
        vpos = i.find('v')
        init = array([int(x) for x in i[2:vpos-1].split(',')])
        velo = array([int(x) for x in i[vpos+2:].split(',')])
        final = (init + j*velo) % array([101, 103])
        robots[final[0]][final[1]] = 1
    if(int(sum(sum(robots))) == 500) : print(j)


robots = [['.' for v in range(101)] for u in range(103)]
for i in inp:
    vpos = i.find('v')
    init = array([int(x) for x in i[2:vpos-1].split(',')])x
    velo = array([int(x) for x in i[vpos+2:].split(',')])
    final = (init + 7687 * velo) % array([101, 103])
    robots[final[1]][final[0]] = '#'

for i in range(len(robots)):
    print(''.join(robots[i]))
