d = {'c1': 'Red', 'c2': 'Green', 'c3': None}

# Initialize an empty list to collect keys to remove
keys_to_remove = []

# Identify keys with None values
for key, value in d.items():
    if value is None:
        keys_to_remove.append(key)
print(keys_to_remove)

# Remove the identified keys
for key in keys_to_remove:
    d.pop(key)

print(d)
