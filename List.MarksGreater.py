d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
x = {}
for keys, values in d.items():
    if values > 170:
        x[keys] = values
print(x)
