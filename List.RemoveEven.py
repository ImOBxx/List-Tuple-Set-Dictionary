l = [1, 2, 3, 4, 5]
"""l = [x for (i, x) in enumerate(l) if i % 2 == 0]
print(l)"""
c = []
for x in l:
    if x % 2 != 0:
        c.append(x)
print(c)
        
