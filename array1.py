class BookStore:
    def __init__(self,title,author,qty,price):
        self.title=title
        self.author=author
        self.qty=qty
        self.price=price
    def getdata(self):
        print("Title",self.title)
        print("Author:",self.author)
        print("qty:",self.qty)
        print("price:",self.price)
books=[]
print("How many books you want to enter")
n=int(input())
for i in range(n):
    print("Enter title, author,qty,price",i+1)
    title=input()
    author=input()
    qty=int(input())
    price=int(input())
    books.append(BookStore(title,author,qty,price))
for book in books:
    print(book.title,book.author,book.qty,book.price)
    #book.get_data()
