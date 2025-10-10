from models import Contact


class ContactOperations:
    def __init__(self, checker, book):
        self.checker = checker
        self.book = book

# Continue working on checking dublicat numbers
    def check_duplicat_number(self, phone_number):
        for contact in self.book.list_of_contacts:
            if contact.phone_number == phone_number:
                print()
                return True
            else:
                print("No dublicats")
                return False

    def create_contact(self):
        contact_name = self.checker.checker_for_empty_important_data(
            input("Name: ").capitalize(), "Name: ")
        company = input("Company: ").capitalize()
        phone_number = self.checker.number_validator(
            input("Phone number: +"), "Phone number: +")
        phone_number = self.check_duplicat_number(phone_number)
        notes = input("Notes: ").capitalize()
        new_contact = Contact(contact_name=contact_name,
                              company=company, phone_number=phone_number,
                              notes=notes)

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
