x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

print(x.isdisjoint(y))
print(y.isdisjoint(z))
print(z.isdisjoint(x))
print(y.isdisjoint(x))
print(x.isdisjoint(z))

# if common found, returns false