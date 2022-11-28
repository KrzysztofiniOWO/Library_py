class Person:
    """Add a customer to our library"""

    backpack = []
    #Backpack to keep books in person's inventory

    def __init__(self):
        """Initialize person class"""

    def show_person_books(self):
        """Show books that person has in inventory"""

        for book in self.backpack:
            for key, value in book.items():
                print(f"{key} - {value}")

    def take_book(self, book):
        """Put book in our backpack after taking it from library"""

        self.backpack.append(book)

    def give_book_back(self, book_id):
        """Take book from person's inventory to return it to library"""

        for book in self.backpack:
            if book["id"] == book_id:
                result = book
                self.backpack.remove(book)
                return result
