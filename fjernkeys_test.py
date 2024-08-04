import json

with open('goodreads_books_without_popular_shelves.json', 'r') as file:
    books = json.load(file)

# List of keys to check for null values
keys_to_check = [
#    "isbn", 
#    "is_ebook", 
#    "kindle_asin", 
#    "link", 
#    "isbn13", 
#    "url", 
#    "image_url",
#    "title", 
#    "country_code",
#    "text_review_count", 
#    "series", 
    "language_code",
#    "popular_shelves", 
#    "asin", 
#    "average_rating", 
    "similar_books", 
    "description",
#    "format", 
    "authors", 
#    "publisher", 
#    "num_pages", 
    "publication_day",
    "publication_month", 
    "publication_year", 
#    "ratings_count", 
#    "edition_information",
    "book_id", 
#    "work_id", 
    "title_without_series"
]

# Filter out books with null values in any of the specified keys
#filtered_books = [
#    book for book in books["books"]
#    if all(book.get(key) is not None for key in keys_to_check)
#]

filtered_books = [
    book for book in books["books"]
    if all((book.get(key) is not "") for key in keys_to_check)
]

# To print books with null values
for book in books["books"]:
    if not all((book.get(key) is not "") for key in keys_to_check):
        print("found book with null value")

# Update the books dictionary
books["books"] = filtered_books

# Saving the updated JSON book back to the file
with open('goodreads_books_final_without_popular_shelves.json', 'w') as file:
    json.dump(books, file, indent=2)

print(f"Done, have a nice day")
print(len(books["books"]))
