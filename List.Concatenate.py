l = ['p', 'q']
n = 5
c = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in l]
print(c)