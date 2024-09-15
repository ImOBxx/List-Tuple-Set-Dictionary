l = [1, 2, 3, 4, 5]
x = [26, 27, 28, 29, 30]
z = []
w = []
r = []
for a in l:
    sum = a * a
    z.append(sum)
for b in x:
    sum = b * b
    w.append(sum)
r = z + w
print(r)

