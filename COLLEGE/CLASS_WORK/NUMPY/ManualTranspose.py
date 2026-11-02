arr = [[98, 99, 111], [121, 44, 95], [10, 15, 77]]

rows = len(arr)
columns = len(arr[0])

transpose = []

for i in range(columns):
    new = []
    for j in range(rows):
        new.append(arr[j][i])
    transpose.append(new)

for row in transpose:
    print(row)
