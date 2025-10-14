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
            phone_number = self.validator.number_validator(
                input("Phone number: +"), "Phone number: +")
            phone_number = self.check.check_duplicat_number(phone_number)
            if phone_number is False:
                continue
            else:
                break
        new_contact = Contact(contact_name=contact_name,
                              phone_number=phone_number)

        self.book.list_of_contacts.append(new_contact)
        print(f"User: {new_contact.contact_name} has been created!")

    def check_contact(self):
        user_input = input("What user do you want to check? ").capitalize()
        checker = self.check.check_user_in_the_list(user_input)
        if checker:
            print(f"User: {user_input} in the phone book!")
        else:
            print(f"User: {user_input} not in the phone book!")

    def edit_contact(self):
        chose = {
            1: "Name",
            2: "Phone number"
        }
        user_input = input("What user do you want to edit? ").capitalize()
        checker = self.check.check_user_in_the_list(user_input)
        index = self.check.return_contact_index(user_input)
        if checker:
            while True:
                for key, value in chose.items():
                    print(f"{key}: {value}")
                user_answer = input("\n What do you want to change? ")
                user_answer = self.validator.checker_for_int(user_answer)
                if user_answer == 1:
                    user_name_input = input(
                        f"What new name for this user: {user_input}? ")
                    self.book.list_of_contacts[index.contact_name] = user_name_input
                    break
                elif user_answer == 2:
                    user_phone_number_input = input(
                        f"What new phone number for this user: {user_input}? ")
                    self.book.list_of_contacts[index.phone_number] = user_phone_number_input
                    break
                else:
                    print("There in no such number, try again!")

    def remove_contact(self):
        user_input = input("What user do you want to remove? ").capitalize()
        checker = self.check.check_user_in_the_list(user_input)
        if checker:
            user_answer = input("Are you sure? y/n")
            user_answer = self.validator.checker_yes_or_no(user_answer)
            if user_answer:
                check_answer = self.check.return_contact(user_input)
                self.book.list_of_contacts.remove(check_answer)
            else:
                return
