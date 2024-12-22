class Book:
    def __init__(self, ISBN, title, author, stock_count):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.__stock_count = stock_count

# Provide read-only access
    def get_stock(self):
        return self.__stock_count

#create add stock method
    def add_stock(self, count):
        if count > 0:
            self.__stock_count += count
            print(f"Stock Count: {self.__stock_count}")
        else:
            print("Invalid Stock addition Count.")

#create borrow book method
    def borrow_book(self):
        if self.__stock_count > 0:
            self.__stock_count -= 1
            print("Book borrowed successfully.")
        else:
            print("No stock available")

    def display_book_info(self):
        print(f"ISBN: {self.ISBN}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Stock: {self.get_stock()}")

#create Object (Book Class)
b1 = Book("23-32-32", "OOP2", "Abdullah", 10)
b1.display_book_info()
b1.borrow_book()
b1.add_stock(7)
