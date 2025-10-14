class Check:
    def __init__(self, book):
        self.book = book

    def check_user_in_the_list(self, user_input: str) -> bool:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == user_input:
                return True
            else:
                continue
        return False

    def return_contact(self, user_input: str) -> object:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == user_input:
                return contact
            else:
                continue

    def return_contact_index(self, user_input: str) -> int:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == user_input:
                index_of_contact = self.book.list_of_contacts.index(contact)
                return index_of_contact
            else:
                continue

    def check_duplicat_number(self, phone_number: str) -> str:
        for contact in self.book.list_of_contacts:
            if contact.phone_number == phone_number:
                print("You already have this number in your phone book")
                return False
            else:
                continue
        return phone_number

    def check_duplicat_names(self, name: str) -> str:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == name:
                print("There is same name already, try another one!")
                return False
            else:
                continue
        return name
