'''
Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears
Check if the string "123abc" is alphanumeric.
'''
a="123abc"
sentence="  i love python programming  "
print(sentence.strip())
print(sentence.title())
print(sentence.count("o"))
print(a.isalnum())

