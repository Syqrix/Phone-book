# This module uses for phone book logic
import sys
from utilities import Validators


class PhoneBookOperations:
    def __init__(self, book, ui, save_json_data):
        self.book = book
        self.ui = ui
        self.save_json_data = save_json_data

    @staticmethod
    def show_contacts(self) -> None:
        if not self.book.list_of_contacts:
            print("There is nothing in the phone book.")
            return None
        else:
            for contact in self.book.list_of_contacts:
                print(f"{contact.contact_name} | {contact.phone_number}")

    @staticmethod
    def clear_phone_book(self) -> None:
        user_wish: str = input("Do you really want to clear phone_book y/n? ")
        checker: bool = Validators.check_y_n_validator(
            user_wish, "Do you really want to clear phone_book y/n? "
        )
        if checker:
            self.book.list_of_contacts.clear()
        else:
            return None

    def exit(self) -> SystemExit:
        self.save_json_data.save_data()
        self.ui.say_bye()
        sys.exit()
