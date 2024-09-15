l =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
"""l.pop(0)
x = l
x.pop(3)
d = x
d.pop(3)
print()
print(d)
print()"""

l = [x for (i, x) in enumerate(l) if i not in (0, 4, 5)] # List Comprehension. 
print(l)