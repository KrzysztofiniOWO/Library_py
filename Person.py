class Person:
    """Add a customer to our library"""

    backpack = []
    #Backpack to keep books in person's inventory

    filename_person = "person.txt"
    #Our database for person

    def __init__(self):
        """Initialize person class"""

    def show_person_books(self):
        """Show books that person has in inventory"""

        for book in self.backpack:
            print("********************")
            for key, value in book.items():
                print(f"{key} - {value}")
            print("********************\n")

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

    def save_person_backpack(self):
        """Save books person has in backpack to a file"""

        with open(self.filename_person, "w") as f:
            for book in self.backpack:
                for key, value in book.items():
                    f.write(f"{key} {value}\n")
        f.close()


    def load_person_backpack(self):
        """Load books person had in backpack from a file"""
