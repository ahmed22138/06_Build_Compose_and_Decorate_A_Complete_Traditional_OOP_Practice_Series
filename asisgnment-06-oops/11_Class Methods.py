
class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment the book count when a new book is created
        Book.increment_book_count()
    # Class method to increment the total book count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("python", "john")
book2 = Book("i am the master of python programming", "john")

print("Total books:", Book.total_books)
