class PhoneBookOperations:
    def __init__(self, contact):
        self.contact = contact

    def check_phone_book(self):
        if not self.phone_book:
            user_wish = input(
                "There is no one in phone book. Do you want to add? ")
            if self.checker.checker_yes_or_no(user_wish):
                self.contact.create_contact()
            else:
                for i in self.phone_book:
                    print(i)

    def clear_phone_book(self):
        user_wish = input("Do you really want to clear phone_book y/n? ")
        if self.checker.checker_yes_or_no(user_wish):
            self.phone_book.clear()
        else:
            return
