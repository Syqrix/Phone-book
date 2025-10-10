# This window for main content of my app
from ui import Comunication
from logic import ContactOperations
from models import PhoneBook, Contact
from utilities import Checker


class App:
    def __init__(self, ui: Comunication, operation: ContactOperations):
        self.ui = ui
        self.operation = operation

    def run(self):
        while True:
            i = 0
            self.ui.say_hi()
            while i < 3:
                self.operation.create_contact()
                self.operation.check_contact("edward")
                i += 1
            self.ui.say_bye()
            break


def main():

    ui = Comunication()
    checker = Checker()
    book = PhoneBook()
    operation = ContactOperations(checker, book)
    app = App(ui, operation)
    app.run()


if __name__ == "__main__":
    main()
