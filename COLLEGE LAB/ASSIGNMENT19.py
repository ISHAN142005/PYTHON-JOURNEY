import pandas as pd

random_dict = {"Mood": ["Happy", "Sad"], "Energy": [10, 2]}
dict_df = pd.DataFrame(random_dict)
print("From dict:\n", dict_df)

dict_df.to_csv("my_vibes.csv", index=False)
csv_load = pd.read_csv("my_vibes.csv")
print("\nFrom CSV:\n", csv_load)
