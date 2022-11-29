import Library as Lib
import Person as Per
import Save as Sav


class Steering:
    """Class to control our library"""

    running = True
    # Check if our library is on/off

    library = Lib.Library()
    #Instance of Library class

    person = Per.Person()
    #Instance of Person class

    save = Sav.Save()
    #Instance of save class

    def __init__(self):
        """Initialize Steering class"""

    def ask_action(self):
        """Ask user what he would like to do next"""

        print("**************************************")
        print("**     Welcome to our library       **")
        print("**   What would you like to do?     **")
        print("**                                  **")
        print("** 1 - Show library books           **")
        print("** 2 - Show book with certain id    **")
        print("** 3 - Borrow a book from library   **")
        print("** 4 - Return a book to library     **")
        print("** 5 - Give away a book to library  **")
        print("** 6 - List of books you borrowed   **")
        print("** 7 - Exit library                 **")
        print("**                                  **")
        print("**************************************\n")

        selected_action = int(input())

        return selected_action

    def steer_library(self):
        """Control our project's behaviour using functions from Library and Person"""

        self.person.load_state_of_backpack(self.save.load_person_backpack())
        self.library.load_state_of_library(self.save.load_library_books())

        while self.running:
            selected_action = self.ask_action()

            if selected_action == 1:
                self.library.show_all_books()

            elif selected_action == 2:
                number = int(input("What is the id of a book you want to see?: "))
                self.library.show_book(number)

            elif selected_action == 3:
                selected = self.library.select_book(int(input("What is the id of a book you want to borrow?: ")))
                self.person.take_book(selected)
                self.library.remove_book(selected)

            elif selected_action == 4:
                selected = self.person.give_book_back(int(input("What is the id of a book you want to give back?: ")))
                self.library.add_book_dict(selected)

            elif selected_action == 5:
                self.library.add_book(self.library.return_number_of_books_in_library() +
                                      self.person.return_number_of_books_in_backpack() + 1)

            elif selected_action == 6:
                self.person.show_person_books()

            elif selected_action == 7:
                self.running = False
                self.save.save_person_backpack(self.person.return_state_of_backpack())
                self.save.save_library_books(self.library.return_state_of_library())
                print("Goodbye.")

            else:
                print("Select proper action")
