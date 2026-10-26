import pandas as pd
import numpy as np

sketchy_banks = pd.DataFrame(
    {
        "Bank_Name": ["Broke Trust", "Empty Vault", "Gone Capital"],
        "City": ["NYC", "London", "Tokyo"],
        "Lost_Money": [1000, np.nan, 5000],
    }
)

print("Original tragedy:\n", sketchy_banks)
print("\nDropping the missing cash row:\n", sketchy_banks.dropna())

grouped_banks = sketchy_banks.groupby("City").sum(numeric_only=True)
print("\nGrouped by city:\n", grouped_banks)
