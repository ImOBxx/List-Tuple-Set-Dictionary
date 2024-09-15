import itertools
l = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
x = list(itertools.chain(*l))
print(x)