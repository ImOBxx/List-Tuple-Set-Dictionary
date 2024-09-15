l = [1, 2, 3, 4, 5]
x = [5, 6, 7, 8 ,9]
c = []
for i in l:
    for j in x:
        if i == j:
            c.append(i)
print(c)
