s = 'w3resource'
d = list(s)
print(d)
x = {}
for i in d:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
print(x)

