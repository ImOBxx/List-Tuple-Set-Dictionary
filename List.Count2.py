n = 3
l = "The Quick Brown Fox"
d = {}
x = []
txt = l.split(" ")
for word in txt:
    print(len(word))
    print(word)
    d[word] = len(word)
    if len(word) > 3:
        x.append(word)
print(d)
print(x)
    