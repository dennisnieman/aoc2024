with open('input.txt') as file:
    inp = file.read().splitlines() 

ans = 0
for i in inp:
    sec = int(i)
    for j in range(2000):
        sec = ((sec*64) ^ sec) % 16777216
        sec = (int(sec/32) ^ sec) % 16777216
        sec = ((sec*2048) ^ sec) % 16777216
    ans += sec
print(ans)


# part 2

scoreList = [0 for x in range(19**4)]
for i in inp:
    indList = []
    diff = []
    sec = int(i)
    for j in range(2000):
        old = sec
        sec = ((sec*64) ^ sec) % 16777216
        sec = (int(sec/32) ^ sec) % 16777216
        sec = ((sec*2048) ^ sec) % 16777216
        diff.append(sec % 10 - old % 10)
        if j>3:
            diff.pop(0)
            ind = ((diff[0]+9) * 19**3 + 
                   (diff[1]+9) * 19**2 + 
                   (diff[2]+9) * 19 +
                   (diff[3]+9))
            if not(ind in indList):
                indList.append(ind)
                scoreList[ind] += sec%10

max(scoreList)