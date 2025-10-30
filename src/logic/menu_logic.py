# This is the main logic of our app
from utilities import Validators


class Menu:
    def __init__(self, phone_book_operations, contact_operations):
        self.phone_book_operations = phone_book_operations
        self.contact_operations = contact_operations

    def choose_the_operation(self):
        while True:
            operations: dict = {
                1: ("Show phone book", self.phone_book_operations.show_contacts),
                2: ("Clear phone book", self.phone_book_operations.clear_phone_book),
                3: ("Create contact", self.contact_operations.create),
                4: ("Check contact", self.contact_operations.check_contact),
                5: ("Edit contact", self.contact_operations.edit),
                6: ("Remove contact", self.contact_operations.remove),
                7: ("Exit", self.phone_book_operations.exit),
            }
            print("\n Avaibal operations:")
            for keys, (text, _) in operations.items():
                print(f"{keys}: {text}")

            while True:
                user_input: str = input("What operation do you want to get? ")
                user_answer: int = Validators.check_int_validator(
                    user_input, "What operation do you want to get? "
                )
                if user_answer not in range(1, 8):
                    print("Not in avaibale range, try again.")
                    continue
                else:
                    break
            _, func = operations[user_answer]
            func()
