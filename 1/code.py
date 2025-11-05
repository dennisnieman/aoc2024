
import pandas as pd
X = pd.read_csv('input.txt', sep="   ", header=None)

# part 1
a1 = pd.array(sorted(X[0]))
a2 = pd.array(sorted(X[1]))
print(sum(abs(a1-a2)))

# part 2
score = 0
for n in a1:
    m = list(a2).count(n)
    score += n*m
print(score)