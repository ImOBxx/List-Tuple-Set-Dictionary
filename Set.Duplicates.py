s = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
l = []
dup = set()
for i in s:
    if i not in dup:
        dup.add(i)
print(dup)

        
