import sys


class PhoneBookOperations:
    def __init__(self, book, validator, ui):
        self.book = book
        self.validator = validator
        self.ui = ui

    def check_phone_book(self):
        if not self.book.list_of_contacts:
            print("There is no one in phone book.")
        else:
            for contact in self.book.list_of_contacts:
                print(f"{contact.contact_name} | +{contact.phone_number}")

    def clear_phone_book(self):
        user_wish = input("Do you really want to clear phone_book y/n? ")
        checker = self.validator.checker_yes_or_no(user_wish)
        if checker:
            self.book.list_of_contacts.clear()
        else:
            return

    def exit_app(self):
        self.ui.say_bye()
        sys.exit()
