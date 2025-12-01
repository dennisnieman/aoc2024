safe = 0
for i in inp:
    report = i.split()
    diffs = list()
    for j in range(len(report)-1):
        diffs.append(int(report[j+1]) - int(report[j]))
    c1 = [d > 0 for d in diffs]
    c2 = [d < 4 for d in diffs]
    c3 = [d < 0 for d in diffs]
    c4 = [d > -4 for d in diffs]
    if (all(c1) and all(c2)) or (all(c3) and all(c4)):
        safe += 1
print(safe)


# part 2
safe = 0
for i in inp:
    report = i.split()
    reports = [report]
    for l in range(len(report)):
        x = report.copy()
        x.pop(l)
        reports.append(x)
    
    flag = 0
    for r in reports:
        diffs = list()
        for j in range(len(r)-1):
            diffs.append(int(r[j+1]) - int(r[j]))
        c1 = [d > 0 for d in diffs]
        c2 = [d < 4 for d in diffs]
        c3 = [d < 0 for d in diffs]
        c4 = [d > -4 for d in diffs]
        if (all(c1) and all(c2)) or (all(c3) and all(c4)):
            flag = 1
    safe += flag
print(safe)
