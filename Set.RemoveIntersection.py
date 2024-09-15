s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
for i in s1 & s2:
    s1.remove(i)
print(s1)
print(s2)