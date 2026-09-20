import json
import pandas as pd


# Load dataset
with open("data/posts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Dataset type:", type(data))
print("Number of records:", len(data))

# Clean invalid Unicode surrogate characters
def clean_text(value):
    if isinstance(value, str):
        return value.encode("utf-8", errors="replace").decode("utf-8")
    elif isinstance(value, list):
        return [clean_text(item) for item in value]
    elif isinstance(value, dict):
        return {key: clean_text(val) for key, val in value.items()}
    return value


data = clean_text(data)

# Convert to DataFrame
df = pd.DataFrame(data)

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset shape:")
print(df.shape)

print("\nFirst record:")
print(df.iloc[0].to_dict())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDataset loaded successfully!")