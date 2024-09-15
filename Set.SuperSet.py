s = {10, 20, 30, 40, 50}
print(s.issuperset(s))      # A set is a superset of itself.

a = {1, 2, 3, 4, 5, 7}
b = {2, 4}
c = {2, 4}
print(a.issuperset(a))
print(a.issuperset(b))
print(c.issuperset(b))
print(a.issuperset(c))
print(b.issuperset(c))

