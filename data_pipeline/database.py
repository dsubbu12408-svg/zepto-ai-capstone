import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("books_cleaned.csv")

# Create SQLite database
conn = sqlite3.connect("books.db")

cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON")

# Create categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE NOT NULL
)
""")

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price_gbp REAL,
    price_inr REAL,
    rating INTEGER,
    in_stock BOOLEAN,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
)
""")

# Insert categories
categories = df["category"].dropna().unique()

for category in categories:
    cursor.execute(
        "INSERT OR IGNORE INTO categories (category_name) VALUES (?)",
        (category,)
    )

# Insert books
for _, row in df.iterrows():

    cursor.execute(
        "SELECT category_id FROM categories WHERE category_name = ?",
        (row["category"],)
    )

    category_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO books
        (title, price_gbp, price_inr, rating, in_stock, category_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        row["title"],
        row["price_gbp"],
        row["price_inr"],
        row["rating"],
        row["in_stock"],
        category_id
    ))

conn.commit()

print("SQLite database created successfully!")
print("Total books:", len(df))
print("Total categories:", len(categories))

conn.close()