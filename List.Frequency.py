l = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)