import sys


class PhoneBookOperations:
    def __init__(self, book, validator, ui, data_manager):
        self.book = book
        self.validator = validator
        self.ui = ui
        self.data_manager = data_manager

    def check_phone_book(self) -> str:
        if not self.book.list_of_contacts:
            print("There is no one in phone book.")
        else:
            for contact in self.book.list_of_contacts:
                print(f"{contact.contact_name} | {contact.phone_number}")

    def clear_phone_book(self):
        user_wish: str = input("Do you really want to clear phone_book y/n? ")
        checker: bool = self.validator.checker_yes_or_no(user_wish)
        if checker:
            self.book.list_of_contacts.clear()
        else:
            return

    def exit_app(self):
        self.data_manager.save_data_to_txt()
        self.ui.say_bye()
        sys.exit()
