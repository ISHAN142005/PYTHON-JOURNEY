weights = list(map(float, input().split()))
average = sum(weights) / len(weights)

count = 0
for weight in weights:
    if weight > average:
        count += 1

print(count)
