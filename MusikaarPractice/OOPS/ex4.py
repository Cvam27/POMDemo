available = ["book1", "book2", "book3", "book4"]
lent_books = []


class Library:

    @staticmethod
    def availbooks(avail_books):
        return avail_books

    @staticmethod
    def lend_book(avail_books, lend_book):
        remove_book = avail_books.remove(lend_book)
        lent_books.append(lend)
        return remove_book

    @staticmethod
    def add_book(new_book):
        new_book = available.append(new_book)

        return new_book

    @staticmethod
    def return_book(returned_book_name):
        return available.append(returned_book_name)

    @staticmethod
    def issued_book():
        return available.remove(lend)


# print("Available books are :", available)
bookstore = Library()
while True:

    print("Available books are :", bookstore.availbooks(available))
    ask = input("Select your choice: Lend book(L) / Return book(R) / Add book(A) :").upper()
    if ask == "L":
        # lend book
        try:
            lend = input("which book to lend?")
            bookstore.lend_book(available, lend_book=lend)
            print("you lent book :", lent_books)

        except:
            print("Invalid book name")
    elif ask == "R":
        # Return Book
        returned = input("which book to return from issued books:")
        if returned in lent_books:
            bookstore.return_book(returned)
            lent_books.remove(returned)
        else:
            print("No such book issued")
    elif ask == "A":
        # Add new book
        add = input("Enter new book name : ")
        bookstore.add_book(add)
