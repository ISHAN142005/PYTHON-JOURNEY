import pandas as pd
import matplotlib.pyplot as plt

reasons_df = pd.DataFrame(
    {"Cause": ["Bad Loans", "Fraud", "Market Crash"], "Amount": [45, 10, 30]}
)

fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
ax.bar(reasons_df["Cause"], reasons_df["Amount"], color="red", alpha=0.6)
ax.set_title("Why They Failed")
ax.legend(["Cases"], loc=3)
plt.show()
