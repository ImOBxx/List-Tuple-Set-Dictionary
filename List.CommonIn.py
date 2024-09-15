print()
l = []
for i in range(1, 6):
    x = int (input ("Enter List 1 Values: "))
    l.append(x)
print(l)
print()
c = []
for i in range(1, 6):
    b = int (input ("Enter List 2 Values: "))
    c.append(b)
print(c)
print()
for a in l:
    for d in c:
        if a == d:
            print("True")\

print()