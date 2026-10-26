import pandas as pd

weird_stats = pd.Series([4, 12, 0, 99], index=["Pizzas", "Coffees", "Naps", "Bugs"])
print("My weekly stats:\n", weird_stats)
print("\nJust the bugs:", weird_stats["Bugs"])

math_stuff = weird_stats * 2
print("\nDoubled for midterms:\n", math_stuff)
