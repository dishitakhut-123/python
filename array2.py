class Book:
    def __init__(self, book_id, title, author, price, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.copies_available = copies_available

    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Copies Available:", self.copies_available)
        print("----------------------------")

    def issue_book(self, quantity):
        if quantity > self.copies_available:
            print("Not enough copies available")
        else:
            self.copies_available -= quantity
            print(quantity, "copies issued successfully")

    def add_copies(self, quantity):
        self.copies_available += quantity
        print(quantity, "copies added successfully")

    def book_value(self):
        return self.price * self.copies_available


# Creating objects
book1 = Book(101, "Python Programming", "Mark Lutz", 750, 5)
book2 = Book(102, "Data Structures and Algorithms", "Thomas H. Cormen", 1200, 3)
book3 = Book(103, "Machine Learning Basics", "Andrew Ng", 950, 4)

# Array (List) of objects
library = [book1, book2, book3]

# Display all books
print("Library Books")
for book in library:
    book.display_book()

# Issue copies of a book
print("Issuing 2 copies of Python Programming")
book1.issue_book(2)

# Add copies to a book
print("Adding 3 copies to Machine Learning Basics")
book3.add_copies(3)

# Calculate total value of all books
total_value = 0
for book in library:
    total_value += book.book_value()

print("Total value of books in library:", total_value)