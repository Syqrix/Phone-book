# This module uses for operations with contacts
from models import Contact
from utilities import Validators


class ContactOperations:
    def __init__(self, book, check_logic):
        self.book = book
        self.check_logic = check_logic

    def create(self) -> None:
        while True:
            contact_name: str = Validators.check_empty_important_data_validator(
                input("Name: ").capitalize(), "Name: "
            )
            contact_name = self.check_logic.check_dublicat_names(contact_name)
            if contact_name is False:
                continue
            else:
                break
        while True:
            phone_number: str = Validators.check_phone_number_validator(
                input("Phone number: +"), "Phone number: +"
            )
            phone_number = self.check_logic.check_dublicat_number(phone_number)
            if phone_number is False:
                continue
            else:
                break
        new_contact: Contact = Contact(
            contact_name=contact_name, phone_number=phone_number
        )

        self.book.list_of_contacts.append(new_contact)
        print(f"User: {new_contact.contact_name} has been created!")

    def check_contact(self) -> None:
        user_input: str = input(
            "What user do you want to check? ").capitalize()
        checker: bool = self.check_logic.check_user_in_the_list(user_input)
        if checker:
            print(f"User: {user_input} is in the phone book!")
        else:
            print(f"User: {user_input} is not in the phone book!")

    def edit(self) -> None:
        chose: dict = {1: "Name", 2: "Phone number"}
        user_input: str = input("What user do you want to edit? ").capitalize()
        checker: bool = self.check_logic.check_user_in_the_list(user_input)
        index: int | None = self.check_logic.return_contact_index(user_input)
        if checker:
            while True:
                for key, value in chose.items():
                    print(f"{key}: {value}")
                user_wish: str = input("\n What do you want to change? ")
                user_answer: int = Validators.check_int_validator(
                    user_wish, "What do you want to change? "
                )
                if user_answer == 1:
                    user_name_input: str = input(
                        f"What new name for this user: {user_input}? "
                    )
                    self.book.list_of_contacts[index].contact_name = (
                        user_name_input.capitalize()
                    )
                    break
                elif user_answer == 2:
                    user_phone_number_input: str = input(
                        f"What new phone number for this user: {user_input}? +"
                    )
                    self.book.list_of_contacts[index].phone_number = (
                        "+" + user_phone_number_input
                    )
                    break
                else:
                    print("There in no such number, try again!")

    def remove(self):
        user_input: str = input(
            "What user do you want to remove? ").capitalize()
        checker: bool = self.check_logic.check_user_in_the_list(user_input)
        if checker:
            user_answer_y_or_n: str = input("Are you sure? y/n ")
            user_answer_on_y_or_n: bool = Validators.check_y_n_validator(
                user_answer_y_or_n, "Are you sure? y/n ")
            if user_answer_on_y_or_n:
                check_answer: str = self.check_logic.return_contact(user_input)
                self.book.list_of_contacts.remove(check_answer)
            else:
                return
