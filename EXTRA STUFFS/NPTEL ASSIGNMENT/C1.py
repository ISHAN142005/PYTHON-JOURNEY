temperatures = list(map(int, input().split()))

if len(temperatures) == 1:
    print(0)
else:
    highest = max(temperatures)
    lowest = min(temperatures)

    print(highest - lowest)
