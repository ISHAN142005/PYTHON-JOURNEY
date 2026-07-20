# Write a program that merges two dictionaries into one

"""
There are mainly three ways of merging dictionary
1.update method
2.{**dictionay1,**dictionay2}
3.| operator  -->In this if dic key have same value then 1 value gets overwritten by 2
"""

Dictionary1 = {
    "Mobile": 10000,
    "Headphone": 2000,
    "Car": 1000000,
    "iPad": 40000,
    "MacBook": 200000,
}

Dictionary2 = {"Cable": 500, "Dongle": 1500, "Connector": 800, "OTG": 300}
merged1 = Dictionary1.update(Dictionary2)
# print(merged1)  This will give None as output
print(Dictionary1)

dic1 = {"Apple": 200, "Banana": 50, "Orange": 180}
dic2 = {"Lemon": 100, "Potato": 20, "Tomato": 50}
merged2 = {**dic1, **dic2}
print(merged2)


name1 = {"Harish": 85, "Satish": 92, "Sam": 78, "Ishan": 100}
name2 = {"Luci": 85, "Kane": 92, "Sam": 88, "Sima": 99}
merged3 = name1 | name2
print(merged3)
