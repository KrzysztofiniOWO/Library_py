class Library:
    """Class to simulate a library"""

    books = []
    # List that keeps all books in our library (book is a dictionary)

    def __int__(self):
        """Initialize Library class"""

    def show_all_books(self):
        for book in self.books:
            print("******************************")
            for key, value in book.items():
                print(f"{key} - {value}")
            print("******************************\n")

    def return_number_of_books_in_library(self):
        """Returns number of books in library"""

        return len(self.books)

    def add_book_dict(self, book):
        """Add book to library after person gave it back"""
        self.books.append(book)

    def add_book(self, id_book):
        """Add book to our library"""

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
            if book["book_id"] == book_id:
                return book

    def show_book(self, book_id):
        """Show book based on its id"""

        print("********************")
        for book in self.books:
            if book["book_id"] == book_id:
                for value, key in book.items():
                    print(f"{key} - {value}")
        else:
            print("there is no such book in our library")
        print("********************\n")

    def return_state_of_library(self):
        """Return list of books we have in library used while saving state of project"""

        return self.books

    def load_state_of_library(self, list_of_books):
        """Load books to library from our database"""

        for book in list_of_books:
            self.books.append(book)
