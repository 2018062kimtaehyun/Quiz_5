scores = [90, 45, 64, 9, 17, 29]

results = []

for score in scores:
    if score >= 71:
        results.append('A')
    elif score >= 41:
        results.append('B')
    elif score >= 11:
        results.append('C')
    else:
        results.append('D')
print(results)
