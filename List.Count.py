n = 3
l = "The Quick Brown Fox Jumps Over The Lazy Dog"
print(len(l))
d = {}
word_len = []
txt = l.split(" ")
print(txt)
for word in txt:
    print(word)
    print(len(word))
    d[word] = len(word)
    if len(word) > n:
        word_len.append(word)
print(word_len)
print(d)

