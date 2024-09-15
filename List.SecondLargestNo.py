l = [1, 2, 3, 4, 5]
x = max(l)
l.pop(4)
b = max(l)
l.pop(3)
l.insert(4, x)
print(l)