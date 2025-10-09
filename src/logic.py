class ContactOperations:
    def create_contact(self):
        self.contact["First name"] = self.first_name
        self.contact["Last name"] = self.last_name
        self.contact["Company"] = self.company
        self.contact["Phone number"] = self.phone_number
        self.contact["Notes"] = self.notes
        self.proces.phone_book.append(self.contact)

    def check_contact(self, contact):
        if contact in self.proces.phone_book:
            return True

    def edit_contact(self, contact: dict):
        if self.check_contact(contact):
            index_of_user = self.proces.phone_book.index(contact)
            changed_user = self.proces.phone_book.copy(index_of_user)
            self.proces.phone_book.remove(contact)
            options = {
                1: "First name",
                2: "Last name",
                3: "Company",
                4: "Phone number",
                5: "Notes"
            }
            print("\n Avaibal operations:")
            for key, value in options.items():
                print(f"{key}: {value}")

            user_wish = int(input("What do you want to change?"))
            # if

        else:
            print("There is no such user in phone book.")

    def remove_contact(self, contact: dict):
        self.proces.phone_book.remove(contact)


class PhoneBookOperations:

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
