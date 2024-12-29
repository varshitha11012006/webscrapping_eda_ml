import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = []
for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.select_one('p.price_color').text
    # availability = book.select_one('p.in_stock.availability').text.strip()
    rating = book.select_one('p.star-rating')['class'][1]  # e.g., 'Three'
    availability = book.select_one('p.in_stock.availability') or None
    if availability:
        availability = availability.text.strip()
    else:
        availability = "Not Available"
    books.append({
        'title': title,
        'price': price,
        'availability': availability,
        'rating': rating
    })
df = pd.DataFrame(books)
print(df.head())
df.to_csv('books_data.csv', index=False)
print("Data saved to books_data.csv")