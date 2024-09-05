import pandas as pd

df = pd.DataFrame({
    "Name": ("Vios", "Raize", "Innova", "Veloz"),
    "Price": ("750k", "950k", "1.1M", "1.5M")
})

print(df.to_string(index=False))