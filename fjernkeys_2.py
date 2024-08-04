import json

with open('inputformatted.json', 'r') as file:
    books = json.load(file)

# key to remove
isbn_remove = "isbn"
ebook_remove = "is_ebook"
kindle_asin_remove = "kindle_asin"
link_remove = "link"
isbn13_remove = "isbn13"
url_remove = "url"
image_url_remove = "image_url"
title_remove = "title"
country_code_remove = "country_code"
popular_shelves_remove = "popular_shelves"
# ----------------------------------------------------------------
text_review_remove = "text_review_count"
series_remove = "series"
country_code_remove = "country_code"
language_code_remove = "language_code"
asin_remove = "asin"
average_rating_remove = "average_rating"
similar_books_remove = "similar_books"
description_remove = "description"
format_remove = "format"
author_remove = "authors"
publisher_remove = "publisher"
num_pages_remove = "num_pages"
publication_day_remove = "publication_day"
publication_month_remove = "publication_month"
publication_year_remove = "publication_year"
ratings_count_remove = "ratings_count"
edition_information_remove = "edition_information"
book_id_remove = "book_id"
work_id_remove = "work_id"
title_without_series_remove = "title_without_series"
# ----------------------------------------------------------------
count = 0
for book in books["books"]:
# checking if the key exists before removing
    count = count + 1
    if count % 1000 == 0:
        print(f"count " + str(count))
    if isbn_remove in book:
        removed_value = book.pop(isbn_remove)
    if ebook_remove in book:
        removed_value = book.pop(ebook_remove)
    if kindle_asin_remove in book:
        removed_value = book.pop(kindle_asin_remove)
    if link_remove in book:
        removed_value = book.pop(link_remove)
    if isbn13_remove in book:
        removed_value = book.pop(isbn13_remove)
    if url_remove in book:
        removed_value = book.pop(url_remove)
    if image_url_remove in book:
        removed_value = book.pop(image_url_remove)
    if title_remove in book:
        removed_value = book.pop(title_remove)
    if country_code_remove in book:
        removed_value = book.pop(country_code_remove)
    if popular_shelves_remove in book:
        removed_value = book.pop(popular_shelves_remove)
print(f"Done, printing")

# saving the updated JSON book back to the file
with open('output_without_popular_shelves.json', 'w') as file:
    json.dump(books, file, indent=2)

print(f"Done printing, have a nice day")