import os
import pandas as pd

# Ensure data/raw directory exists
os.makedirs("data/raw", exist_ok=True)

url = "https://raw.githubusercontent.com/ChicagoBoothML/MLClassData/master/GiveMeSomeCredit/CreditScoring.csv"
save_path = "data/raw/cs-training.csv"

print("Downloading dataset...")
df = pd.read_csv(url)

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

df.to_csv(save_path, index=False)
print(f"Success! Saved {df.shape[0]} rows and {df.shape[1]} columns to {save_path}")