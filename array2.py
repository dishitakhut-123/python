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


book1 = Book(101, "Python Programming", "Mark Lutz", 750, 5)
book2 = Book(102, "Data Structures and Algorithms", "Thomas H. Cormen", 1200, 3)
book3 = Book(103, "Machine Learning Basics", "Andrew Ng", 950, 4)

library = [book1, book2, book3]

library.sort(key=lambda book: book.price, reverse=True)

print("Library Books (Descending Order by Price)")
for book in library:
    book.display_book()

print("Issuing 2 copies of Python Programming")
book1.issue_book(2)

print("Adding 3 copies to Machine Learning Basics")
book3.add_copies(3)

total_value = 0
for book in library:
    total_value += book.book_value()

print("Total value of books in library:", total_value)