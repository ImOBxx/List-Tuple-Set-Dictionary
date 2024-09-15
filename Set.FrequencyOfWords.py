words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
count = 0
d = {}
for c in words:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
print(d)