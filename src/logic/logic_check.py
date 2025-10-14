class Check:
    def __init__(self, book):
        self.book = book

    def check_duplicat_number(self, phone_number):
        for contact in self.book.list_of_contacts:
            if contact.phone_number == phone_number:
                print("You already have this number in your phone book")
                return False
            else:
                continue
        print("No dublicats")
        return phone_number

    def check_duplicat_names(self, name):
        for contact in self.book.list_of_contacts:
            if contact.contact_name == name:
                print("There is same name already, try another one!")
                return False
            else:
                continue
        print("No dublicats")
        return name
