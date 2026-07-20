# Given a dictionary of products and their prices, find the product with the highest price.

Dictionary1 = {"Mobile": 10000, "Laptop": 50000, "Car": 1000000, "Scooty": 150000}

HighrstPricedProduct = max(Dictionary1, key=Dictionary1.get)

'''
key= tells Python how to compare the elements.

Dictionary1.get is a function that, given a key, returns its value.
'''
print("Product with the highest price:", HighrstPricedProduct)
print("Highest price:", Dictionary1[HighrstPricedProduct])
