# This is the main logic of our app
from abc import ABC, abstractmethod


class Menu(ABC):
    def __init__(self, int_validator, check_phone_book, clear_phone_book,
                 exit_phone_book, create_contact, check_contact, edit_contact,
                 remove_contact):
        self.int_validator = int_validator
        self.check_phone_book = check_phone_book
        self.clear_phone_book = clear_phone_book
        self.exit_phone_book = exit_phone_book
        self.create_contact = create_contact
        self.check_contact = check_contact
        self.edit_contact = edit_contact
        self.remove_contact = remove_contact

    @abstractmethod
    def operation(self):
        pass


class ChooseOperation(Menu):

    def operation(self):
        while True:
            operations: dict = {
                1: ("Check phone book", self.check_phone_book.phone_book_operation),
                2: ("Clear phone book", self.clear_phone_book.phone_book_operation),
                3: ("Create contact", self.create_contact.operation),
                4: ("Check contact", self.check_contact.operation),
                5: ("Edit contact", self.edit_contact.operation),
                6: ("Remove contact", self.remove_contact.operation),
                7: ("Exit", self.exit_phone_book.phone_book_operation)
            }
            print("\n Avaibal operations:")
            for keys, (desc, _) in operations.items():
                print(f"{keys}: {desc}")

            while True:
                user_input: str = input("What operation do you want to get? ")
                user_input: int = self.int_validator.validation(
                    user_input, "What operation do you want to get? ")
                if user_input not in range(1, 8):
                    print("Not in avaibale range, try again.")
                    continue
                else:
                    break
            _, func = operations[user_input]
            func()
