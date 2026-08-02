numbers = input().split()
even_count = 0

for num in numbers:
    if int(num) % 2 == 0:
        even_count += 1

print(even_count)
