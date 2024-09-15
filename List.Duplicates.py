l = [1, 2, 3, 4, 5, 3, 4, 2, 4, 7,]
x = []
for i in l:
    if i not in x:
        x.append(i)
print(x)