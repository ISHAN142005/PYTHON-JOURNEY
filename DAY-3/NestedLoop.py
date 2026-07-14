# Example of Nested Loop: Multiplication Table (1 to 5)

for i in range(1, 6):          # outer loop → rows
    for j in range(1, 6):      # inner loop → columns
        print(i * j, end="\t") # print product with tab spacing
    print()                    # move to next line after each row


'''
Output-
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25

'''