class Person:
    """Add a customer to our library"""

    backpack = []
    #Backpack to keep books in person's inventory

    def __init__(self):
        """Initialize person class"""

    def show_person_books(self):
        """Show books that person has in inventory"""

        for book in self.backpack:
            print("********************")
            for key, value in book.items():
                print(f"{key} - {value}")
            print("********************\n")

    def return_number_of_books_in_backpack(self):
        """Returns number of books in backpack"""

        return len(self.backpack)

    def take_book(self, book):
        """Put book in our backpack after taking it from library"""

        self.backpack.append(book)

    def give_book_back(self, book_id):
        """Take book from person's inventory to return it to library"""

        for book in self.backpack:
            if book["book_id"] == book_id:
                result = book
                self.backpack.remove(book)
                return result

    def return_state_of_backpack(self):
        """Return list of books we have in backpack used while saving state of project"""

        return self.backpack

    def load_state_of_backpack(self, list_of_books):
        """Load books to library from our database"""

        for book in list_of_books:
            self.backpack.append(book)
