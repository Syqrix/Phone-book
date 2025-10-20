# This window for main content of my app
from ui import SayHi, SayBye
from logic import ChooseOperation
from models import PhoneBook
from utilities import Validator, Check


class App:
    def __init__(self, say_hi: SayHi, say_bye: SayBye,
                 choose_operation: ChooseOperation, data_manager: DataManager):
        self.say_hi = say_hi
        self.say_bye = say_bye
        self.choose_operation = choose_operation
        self.data_manager = data_manager

    def run(self):
        while True:
            self.data_manager.load_data()
            self.say_hi.say()
            self.choose_operation.operation()
            self.say_bye.say()


def main():
    say_hi = SayHi()
    say_bye = SayBye()
    chose_operation = ChooseOperation()
    validator = Validator()
    book = PhoneBook()
    data_manager = DataManager(book)
    check = Check(book)
    contact_operation = ContactOperations(validator, book, check)
    phone_book_operation = PhoneBookOperations(
        book, validator, ui, data_manager)
    menu = Menu(validator, contact_operation, phone_book_operation)
    app = App(say_hi, say_bye,  chose_operation, data_manager)
    app.run()


if __name__ == "__main__":
    main()
