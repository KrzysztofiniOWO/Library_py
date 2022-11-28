import Library as Lib


class Steering:
    """Class to control our library"""

    running = True
    # Check if our library is on/off

    library = Lib.Library()
    #Instance of Library class

    def __init__(self):
        """Initialize Steering class"""

    def ask_action(self):
        """Ask user what he would like to do next"""

        print("**************************************")
        print("**     Welcome to our library       **")
        print("**   What would you like to do?     **")
        print("**                                  **")
        print("** 1 - Show all books               **")
        print("** 2 - Show book with certain id    **")
        print("** 3 - Borrow a book from library   **")
        print("** 4 - Return a book to library     **")
        print("** 5 - Give away a book to library  **")
        print("** 6 - Exit library                 **")
        print("**                                  **")
        print("**************************************\n")

        selected_action = int(input())

        return selected_action

    def steer_library(self):
        """Control our project's behaviour using functions from Library and Person"""

        while self.running:
            selected_action = self.ask_action()

            if selected_action == 1:
                self.library.show_all_books()

            elif selected_action == 2:
                print("b")

            elif selected_action == 3:
                print("c")

            elif selected_action == 4:
                print("d")

            elif selected_action == 5:
                self.library.add_book()

            elif selected_action == 6:
                self.running = False
                print("Goodbye.")

            else:
                print("Select proper action")
