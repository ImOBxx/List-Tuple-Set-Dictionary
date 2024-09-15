d = {'a' : 1, 'b': 2, 'c': 3, 'd': 4}
"""if 'a' in d:
    del d['a']

print(d)"""

for i in d:
    if d[i] == 'a':
        d.popitem('a')

print(d)
