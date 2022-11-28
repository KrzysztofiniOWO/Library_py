class Library:
    """Class to simulate a library"""

    books = []
    # List that keeps all books in our library (book is a dictionary)

    def __int__(self):
        """Initialize Library class"""

    def load_library(self):
        """Load books to our library from a save file"""

    def show_all_books(self):
        for book in self.books:
            print("******************************")
            for key, value in book.items():
                print(f"{key} - {value}")
            print("******************************\n")

    def add_book_dict(self, book):
        """Add book to library after person gave it back"""
        self.books.append(book)

    def add_book(self):
        """Add book to our library"""

        id_book = (len(self.books) + 1)
        title_book = input("What is the title of book you want to add?: ")
        type_book = Library.select_type(self)
        number_pages = int(input("What is the number of pages of your book?: "))

        book = {"book_id": id_book, "book_title": title_book, "book_type": type_book, "number_of_pages": number_pages, }
        self.books.append(book)

    def select_type(self):
        """Select the type of book you want to add"""

        genres = ["action", "fantasy", "thriller", "horror", "historical", "drama", "comedy", "biography", "scientific"]

        for number in range(0, len(genres)):
            print(f"{number + 1} - {genres[number]}")

        selected = int(input("What is the type of book you want to add?: "))
        return genres[selected - 1]

    def remove_book(self, book):
        """Remove book from our library"""

        self.books.remove(book)

    def select_book(self, book_id):
        """Select a book to do something with it in another function (for example borrow it)"""

        for book in self.books:
            if book["id"] == book_id:
                return book

    def show_book(self, book_id):
        """Show book based on its id"""

        print("********************")

        for book in self.books:
            if book["id"] == book_id:
                for value, key in book.items():
                    print(f"{key} - {value}")
        else:
            print("there is no such book in our library")
        print("********************")
