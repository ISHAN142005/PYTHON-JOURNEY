import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales_mess = pd.DataFrame(
    {"Month": ["Jan", "Feb", "Mar", "Apr"], "Revenue": [100, 150, 80, 200]}
)

sns.set_theme(style="darkgrid")
color_pick = sns.color_palette("pastel")

sns.barplot(x="Month", y="Revenue", data=sales_mess, palette=color_pick)
plt.title("Company Money Moves")
plt.show()
