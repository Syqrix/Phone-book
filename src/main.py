# This window for main content of my app
from ui import Comunication
from logic import ContactOperations, Check
from models import PhoneBook
from utilities import Validator


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
                i += 1
            self.ui.say_bye()
            break


def main():

    ui = Comunication()
    validator = Validator()
    book = PhoneBook()
    check = Check(book)
    operation = ContactOperations(validator, book, check)
    app = App(ui, operation)
    app.run()


if __name__ == "__main__":
    main()
