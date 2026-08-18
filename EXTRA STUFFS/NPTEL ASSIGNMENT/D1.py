product_ids = list(map(int, input().split()))
print(len(product_ids) != len(set(product_ids)))