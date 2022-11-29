class Save:
    """Class to save and load book for library and person"""

    filename_person = "person.txt"
    filename_library = "library.txt"

    # Our databases for person and library

    def __init__(self):
        """Initialize save class"""

    def save_person_backpack(self, backpack):
        """Save books person has in backpack to a file"""

        with open(self.filename_person, "w") as f:
            for book in backpack:
                for key, value in book.items():
                    f.write(f"{key} {value}\n")
        f.close()

    def load_person_backpack(self):
        """Load books person had in backpack from a file"""

        list_of_books = []
        book = {}
        it = 0

        with open(self.filename_person, "r") as f:
            for line in f:
                (key, val) = line.split()
                book[key] = val
                it = it + 1
                if it % 4 == 0:
                    list_of_books.append(book)
                    book = {}
        return list_of_books

    def save_library_books(self, books):
        """Save books from our library to a file"""

        with open(self.filename_library, "w") as f:
            for book in books:
                for key, value in book.items():
                    f.write(f"{key} {value}\n")
        f.close()

    def load_library_books(self):
        """Load books library had from a file"""

        list_of_books = []
        book = {}
        it = 0

        with open(self.filename_library, "r") as f:
            for line in f:
                (key, val) = line.split()
                book[key] = val
                it = it + 1
                if it % 4 == 0:
                    list_of_books.append(book)
                    book = {}
        return list_of_books
