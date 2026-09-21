import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("books.db")

print("\n--- QUERY 1: Total books ---")
q1 = "SELECT COUNT(*) AS total_books FROM books"
print(pd.read_sql(q1, conn))

print("\n--- QUERY 2: Average price in INR ---")
q2 = "SELECT ROUND(AVG(price_inr), 2) AS average_price_inr FROM books"
print(pd.read_sql(q2, conn))

print("\n--- QUERY 3: Books by rating ---")
q3 = """
SELECT rating, COUNT(*) AS book_count
FROM books
GROUP BY rating
ORDER BY rating
"""
print(pd.read_sql(q3, conn))

print("\n--- QUERY 4: Books by category ---")
q4 = """
SELECT c.category_name, COUNT(*) AS book_count
FROM books b
JOIN categories c
ON b.category_id = c.category_id
GROUP BY c.category_name
ORDER BY book_count DESC
"""
print(pd.read_sql(q4, conn))

print("\n--- QUERY 5: Books in stock ---")
q5 = """
SELECT COUNT(*) AS in_stock_books
FROM books
WHERE in_stock = 1
"""
print(pd.read_sql(q5, conn))

print("\n--- QUERY 6: Top 10 expensive books ---")
q6 = """
SELECT title, price_inr
FROM books
ORDER BY price_inr DESC
LIMIT 10
"""
print(pd.read_sql(q6, conn))

print("\n--- QUERY 7: JOIN books with categories ---")
join_query = """
SELECT
    b.title,
    b.price_inr,
    b.rating,
    c.category_name
FROM books b
JOIN categories c
ON b.category_id = c.category_id
LIMIT 10
"""

join_result = pd.read_sql(join_query, conn)
print(join_result)

print("\n--- pandas.merge reproduction of JOIN ---")

books_df = pd.read_sql("SELECT * FROM books", conn)
categories_df = pd.read_sql("SELECT * FROM categories", conn)

merge_result = books_df.merge(
    categories_df,
    on="category_id",
    how="inner"
)

print(
    merge_result[
        ["title", "price_inr", "rating", "category_name"]
    ].head(10)
)

conn.close()

print("\nAll SQL queries completed successfully!")