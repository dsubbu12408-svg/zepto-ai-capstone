import pandas as pd

# Load scraped data
df = pd.read_csv("books.csv")

# Clean price
df["price_gbp"] = pd.to_numeric(
    df["price"].astype(str).str.replace(r"[^0-9.]", "", regex=True),
    errors="coerce"
)

# Clean rating
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

# Convert availability to True/False
df["in_stock"] = (
    df["availability"]
    .astype(str)
    .str.contains("In stock", case=False, na=False)
)

# Convert GBP to INR
df["price_inr"] = (df["price_gbp"] * 110).round(2)

# Keep required columns
df = df[
    [
        "title",
        "price_gbp",
        "price_inr",
        "rating",
        "in_stock",
        "category"
    ]
]

# Save cleaned data
df.to_csv("books_cleaned.csv", index=False)

print("Cleaning completed successfully!")
print(f"Total books: {len(df)}")
print("Saved as: books_cleaned.csv")
print(df.head())