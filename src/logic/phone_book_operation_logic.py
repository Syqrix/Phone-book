# This module uses for phone book logic
import sys
from abc import ABC, abstractmethod


class PhoneBookOperation(ABC):
    def __init__(self, book=None, yes_no_validator=None, say_bye=None, save_json_data=None):
        self.book = book
        self.yes_no_validator = yes_no_validator
        self.say_bye = say_bye
        self.save_json_data = save_json_data

    @abstractmethod
    def phone_book_operation(self):
        pass


class CheckPhoneBook(PhoneBookOperation):
    def __init__(self, book):
        super().__init__(book=book)

    def phone_book_operation(self) -> str:
        if not self.book.list_of_contacts:
            print("There is no one in phone book.")
        else:
            for contact in self.book.list_of_contacts:
                print(f"{contact.contact_name} | {contact.phone_number}")


class ClearPhoneBook(PhoneBookOperation):
    def __init__(self, book, yes_no_validator):
        super().__init__(book=book, yes_no_validator=yes_no_validator)

    def phone_book_operation(self):
        user_wish: str = input("Do you really want to clear phone_book y/n? ")
        checker: bool = self.yes_no_validator.validation(user_wish)
        if checker:
            self.book.list_of_contacts.clear()
        else:
            return


class ExitPhoneBook(PhoneBookOperation):
    def __init__(self, save_json_data, say_bye):
        super().__init__(save_json_data=save_json_data, say_bye=say_bye)

    def phone_book_operation(self):
        self.save_json_data.save_data()
        self.say_bye.say()
        sys.exit()
