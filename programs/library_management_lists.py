# List of available books in the library
available_books = [
    "The Alchemist",
    "1984",
    "Python Crash Course",
    "Clean Code",
    "To Kill a Mockingbird"
]

# List to track issued books
issued_books = []

# List to track returned books
returned_books = []

# Function to issue a book
def issue_book(book_name):
    if book_name in available_books:
        available_books.remove(book_name)
        issued_books.append(book_name)
        print(f"Issued: {book_name}")
    else:
        print(f"Sorry, '{book_name}' is not available.")

# Function to return a book
def return_book(book_name):
    if book_name in issued_books:
        issued_books.remove(book_name)
        returned_books.append(book_name)
        available_books.append(book_name)
        print(f"Returned: {book_name}")
    else:
        print(f"'{book_name}' was not issued.")

# Display current status
def show_status():
    print("\nAvailable Books:", available_books)
    print("Issued Books:", issued_books)
    print("Returned Books:", returned_books)

# Real-life usage simulation
show_status()
issue_book("1984")
issue_book("Python Crash Course")
show_status()
return_book("1984")
show_status()
