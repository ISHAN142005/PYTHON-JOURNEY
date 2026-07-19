num={2,8,9,11,0,123}
print(num)

num.add(99)   #--> Will add entered number at random position
print(num) 
num.add(99)   #--> This will not make any change in set as 99 is already present
print(num) 
num.add(100)
print(num) 

num.update([1,3])   #-->Adds multiple elements
print(num)

num.remove(99)  #Removes element (error if not found)

num.discard(123) #Removes element (no error if missing)

num.pop()
print(num)

num.clear()
print(num) #-->Clears the entire set

