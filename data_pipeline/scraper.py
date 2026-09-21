import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
URL = BASE_URL

books = []

while URL:
    print(f"Scraping: {URL}")

    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=20
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]
        price = item.select_one(".price_color").get_text(strip=True)
        rating = item.select_one("p.star-rating")["class"][1]
        availability = item.select_one(".availability").get_text(" ", strip=True)

        category = "Unknown"
        product_link = urljoin(BASE_URL, item.h3.a["href"])

        product_response = requests.get(
            product_link,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20
        )

        product_soup = BeautifulSoup(product_response.text, "html.parser")

        breadcrumb = product_soup.select("ul.breadcrumb li")
        if len(breadcrumb) >= 3:
            category = breadcrumb[2].get_text(strip=True)

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "category": category
        })

        if len(books) >= 100:
            break

    if len(books) >= 100:
        break

    next_button = soup.select_one("li.next a")

    if next_button:
        URL = urljoin(URL, next_button["href"])
    else:
        URL = None

print(f"\nTotal books collected: {len(books)}")

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "title",
            "price",
            "rating",
            "availability",
            "category"
        ]
    )

    writer.writeheader()
    writer.writerows(books)

print("Data saved successfully to books.csv")
print("Categories found:", len(set(book["category"] for book in books)))