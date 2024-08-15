import json

def process_large_json(input_file, output_file):
    links = []
    nodes = []

    with open(input_file, 'r') as f:
        data = json.load(f)
        books = data["books"]

        for book in books:
            book_id = int(book["book_id"])
            node = {
                "text_reviews_count": book.get("text_reviews_count", ""),
                "series": book.get("series", []),
                "language_code": book.get("language_code", ""),
                "asin": book.get("asin", ""),
                "average_rating": book.get("average_rating", ""),
                "similar_books": [int(sb) for sb in book.get("similar_books", [])],
                "description": book.get("description", ""),
                "format": book.get("format", ""),
                "authors": book.get("authors", []),
                "publisher": book.get("publisher", ""),
                "num_pages": book.get("num_pages", ""),
                "publication_day": book.get("publication_day", ""),
                "publication_month": book.get("publication_month", ""),
                "edition_information": book.get("edition_information", ""),
                "publication_year": book.get("publication_year", ""),
                "book_id": book_id,
                "ratings_count": book.get("ratings_count", ""),
                "work_id": book.get("work_id", ""),
                "title_without_series": book.get("title_without_series", "")
            }
            nodes.append(node)
            for target in book["similar_books"]:
                links.append({"source": book_id, "target": int(target)})

    with open(output_file, 'w') as f:
        output = {
            "nodes": nodes,
            "links": links
        }
        json.dump(output, f, indent=4)

def main():
    input_file = 'goodreads_books_final_without_popular_shelves.json'
    output_file = '25000_nodes_and_links_sofie.json'
    process_large_json(input_file, output_file)

if __name__ == "__main__":
    main()
