pages_input = input().split()
senior_books = []

for page in pages_input:
    if int(page) > 300:
        senior_books.append(page)

print(" ".join(senior_books))