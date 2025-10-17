# This window for main content of my app
from ui import Comunication
from logic import ContactOperations, PhoneBookOperations, Menu, DataManager
from models import PhoneBook
from utilities import Validator, Check


class App:
    def __init__(self, ui: Comunication, menu: Menu, data_manager: DataManager):
        self.ui = ui
        self.menu = menu
        self.data_manager = data_manager

    def run(self):
        while True:
            self.data_manager.load_data()
            self.ui.say_hi()
            self.menu.user_wish()
            self.ui.say_bye()


def main():
    ui = Comunication()
    validator = Validator()
    book = PhoneBook()
    data_manager = DataManager(book)
    check = Check(book)
    contact_operation = ContactOperations(validator, book, check)
    phone_book_operation = PhoneBookOperations(
        book, validator, ui, data_manager)
    menu = Menu(validator, contact_operation, phone_book_operation)
    app = App(ui, menu, data_manager)
    app.run()


if __name__ == "__main__":
    main()
