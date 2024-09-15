l = ["Python", "Exercises", "Practice", "Solution", "Exercises"]
dup = set()
for i in l:
    if i not in dup:
        dup.add(i)
print(dup)