str = "Splitter"
s = []
d = {}
txt = str.split()
for c in str:
    print(c)
    s.append(c)
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print(s)
print(d)