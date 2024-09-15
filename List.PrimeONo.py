"""l = [2, 3, 5, 15, 7, 11, 13, 18, 17, 19, 23, 21]
c = []
count = 0
for i in l:
    for x in range(1, i + 1):
        if i % x == 0:
            count += 1
        if count == 2:
            c.append(x)
            print(c)"""


l = [2, 3, 5, 15, 7, 11, 13, 18, 17, 19, 23, 21]
c = []

for i in l:
    count = 0
    for x in range(1, i + 1):
        if i % x == 0:
            count += 1
    if count == 2:  
        c.append(i)
print(c)



