d = {"V":"S001", "V2": "S002", "VI": "S001", "VI2": "S005", "VII":"S005", "V3":"S009", "VIII":"S007"}
s = {}
for keys, values in d.items():
     if keys not in s:
      s[keys] = values

print(s)
    
