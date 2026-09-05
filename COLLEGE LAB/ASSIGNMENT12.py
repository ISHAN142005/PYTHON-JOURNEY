car_info = {"maker": "Land Rover", "model": "Defender", "year": 2022}
print("Car details:", car_info)

dict_length = len(car_info)
print("\nTotal items:", dict_length)

car_info["color"] = "Green"
print("\nAdded color:", car_info)

car_info.pop("year")
print("Removed year:", car_info)

car_info_copy = car_info.copy()
print("\nCopied details:", car_info_copy)
