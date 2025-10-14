from models import Contact


class ContactOperations:
    def __init__(self, validator, book, check):
        self.validator = validator
        self.book = book
        self.check = check

    def create_contact(self):
        while True:
            contact_name = self.validator.checker_for_empty_important_data(
                input("Name: ").capitalize(), "Name: ")
            contact_name = self.check.check_duplicat_names(contact_name)
            if contact_name is False:
                continue
            else:
                break
        while True:
            phone_number = self.validators.number_validator(
                input("Phone number: +"), "Phone number: +")
            phone_number = self.check.check_duplicat_number(phone_number)
            if phone_number is False:
                continue
            else:
                break
        new_contact = Contact(contact_name=contact_name,
                              phone_number=phone_number)

        self.book.list_of_contacts.append(new_contact)

    def check_contact(self, contact):
        if contact not in self.book.list_of_contacts:
            print("There is no such user in the phone book!")
        else:
            print(f"User: {contact} in the phone book")
            # def edit_contact(self):
            #     if self.check_contact(contact):
            #         index_of_user = self.proces.phone_book.index(contact)
            #         changed_user = self.proces.phone_book.copy(index_of_user)
            #         self.proces.phone_book.remove(contact)
            #         options = {
            #             1: "First name",
            #             2: "Last name",
            #             3: "Company",
            #             4: "Phone number",
            #             5: "Notes"
            #         }
            #         print("\n Avaibal operations:")
            #         for key, value in options.items():
            #             print(f"{key}: {value}")

            #         user_wish = int(input("What do you want to change?"))
            #         # if

            #     else:
            #         print("There is no such user in phone book.")

            # def remove_contact(self, contact: dict):
            #     self.proces.phone_book.remove(contact)
