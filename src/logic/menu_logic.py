# This is the main logic of our app
from abc import ABC, abstractmethod


class Menu(ABC):
    def __init__(self, validator, contact_operation, phone_book_operation):
        self.validator = validator
        self.contact_operation = contact_operation
        self.phone_book_operation = phone_book_operation

    @abstractmethod
    def operation(self):
        pass


class ChooseOperation(Menu):
    def operation(self):
        while True:
            operations: dict = {
                1: ("Check phone book", self.phone_book_operation.check_phone_book),
                2: ("Clear phone book", self.phone_book_operation.clear_phone_book),
                3: ("Create contact", self.contact_operation.create_contact),
                4: ("Check contact", self.contact_operation.check_contact),
                5: ("Edit contact", self.contact_operation.edit_contact),
                6: ("Remove contact", self.contact_operation.remove_contact),
                7: ("Exit", self.phone_book_operation.exit_app)
            }
            print("\n Avaibal operations:")
            for keys, (desc, _) in operations.items():
                print(f"{keys}: {desc}")

            while True:
                user_input: str = input("What operation do you want to get? ")
                user_input: int = self.validator.checker_for_int(
                    user_input, "What operation do you want to get? ")
                if user_input not in range(1, 8):
                    print("Not in avaibale range, try again.")
                    continue
                else:
                    break
            _, func = operations[user_input]
            func()
