# 11. Class Methods ;

# Assignment:

# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book():
    total_books = 0

    def __init__(self, title, author):
       self.title = title
       self.author = author
       Book.increment_book_count()
    @classmethod
    def increment_book_count(cls):
        # Class method to update the total_books count
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        # Class method to retrieve the total book count
        return cls.total_books
    

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Display the total book count
print(f"Total books added: {Book.get_total_books()}")