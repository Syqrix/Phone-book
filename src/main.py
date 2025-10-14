# This window for main content of my app
from ui import Comunication
from logic import ContactOperations, PhoneBookOperations, Menu
from models import PhoneBook
from utilities import Validator, Check


class App:
    def __init__(self, ui: Comunication, menu: Menu):
        self.ui = ui
        self.menu = menu

    def run(self):
        while True:
            self.ui.say_hi()
            self.menu.user_wish()
            self.ui.say_bye()


def main():

    ui = Comunication()
    validator = Validator()
    book = PhoneBook()
    check = Check(book)
    contact_operation = ContactOperations(validator, book, check)
    phone_book_operation = PhoneBookOperations(book, validator, ui)
    menu = Menu(validator, contact_operation, phone_book_operation)
    app = App(ui, menu)
    app.run()


if __name__ == "__main__":
    main()
