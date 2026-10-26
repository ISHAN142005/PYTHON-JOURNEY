import pandas as pd
import matplotlib.pyplot as plt

bank_ruins = pd.DataFrame(
    {"Year": [2008, 2009, 2010, 2011], "Failures": [25, 140, 157, 92]}
)

fig, ax1 = plt.subplots()
ax1.plot(bank_ruins["Year"], bank_ruins["Failures"], "b.-", label="Crashes")
ax1.set_xlabel("Bad Years")
ax1.set_ylabel("Number of Bankruptcies")
ax1.set_title("Banks Going Under")
plt.show()
