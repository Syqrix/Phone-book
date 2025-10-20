# This module uses for operations with contacts
from models import Contact
from abc import ABC, abstractmethod


class ContactOperation(ABC):
    def __init__(
            self, book=None, empty_check_validator=None, number_validator=None,
            int_validator=None, yes_no_validator=None,
            check_duplicat_names=None, check_dublicat_number=None,
            check_user_in_the_list=None, return_contact_index=None,
            return_contact=None):
        self.empty_check_validator = empty_check_validator
        self.int_validator = int_validator
        self.number_validator = number_validator
        self.yes_no_validator = yes_no_validator
        self.check_duplicat_names = check_duplicat_names
        self.check_dublicat_number = check_dublicat_number
        self.check_user_in_the_list = check_user_in_the_list
        self.return_contact_index = return_contact_index
        self.return_contact = return_contact
        self.book = book

    def operation(self):
        pass


class CreateContact(ContactOperation):
    def __init__(
            self, book, empty_check_validator, number_validator,
            check_duplicat_names, check_dublicat_number):
        super().__init__(
            book=book, empty_check_validator=empty_check_validator,
            number_validator=number_validator, check_duplicat_names=check_duplicat_names,
            check_dublicat_number=check_dublicat_number)

    def operation(self) -> object:
        while True:
            contact_name: str = self.empty_check_validator.validation(
                input("Name: ").capitalize(), "Name: ")
            contact_name: str = self.check_duplicat_names.logic_check_operation(
                contact_name)
            if contact_name is False:
                continue
            else:
                break
        while True:
            phone_number: str = self.number_validator.validation(
                input("Phone number: +"), "Phone number: +")
            phone_number: str = self.check_dublicat_number.logic_check_operation(
                phone_number)
            if phone_number is False:
                continue
            else:
                break
        new_contact: object = Contact(contact_name=contact_name,
                                      phone_number=phone_number)

        self.book.list_of_contacts.append(new_contact)
        print(f"User: {new_contact.contact_name} has been created!")


class CheckContact(ContactOperation):
    def __init__(
            self, check_user_in_the_list):
        super().__init__(check_user_in_the_list=check_user_in_the_list)

    def operation(self) -> str:
        user_input: str = input(
            "What user do you want to check? ").capitalize()
        checker: bool = self.check_user_in_the_list.logic_check_operation(
            user_input)
        if checker:
            print(f"User: {user_input} is in the phone book!")
        else:
            print(f"User: {user_input} is not in the phone book!")


class EditContact(ContactOperation):
    def __init__(
            self, book, int_validator, check_user_in_the_list, return_contact_index):
        super().__init__(
            book=book, int_validator=int_validator,
            check_user_in_the_list=check_user_in_the_list,
            return_contact_index=return_contact_index)

    def operation(self) -> str:
        chose: dict = {
            1: "Name",
            2: "Phone number"
        }
        user_input: str = input("What user do you want to edit? ").capitalize()
        checker: bool = self.check_user_in_the_list.logic_check_operation(
            user_input)
        index: int = self.return_contact_index.logic_check_operation(
            user_input)
        if checker:
            while True:
                for key, value in chose.items():
                    print(f"{key}: {value}")
                user_answer: str = input("\n What do you want to change? ")
                user_answer: int = self.int_validator.validation(
                    user_answer, "What do you want to change? ")
                if user_answer == 1:
                    user_name_input: str = input(
                        f"What new name for this user: {user_input}? ")
                    self.book.list_of_contacts[index].contact_name = user_name_input.capitalize(
                    )
                    break
                elif user_answer == 2:
                    user_phone_number_input: str = input(
                        f"What new phone number for this user: {user_input}? ")
                    self.book.list_of_contacts[index].phone_number = "+" + \
                        user_phone_number_input
                    break
                else:
                    print("There in no such number, try again!")


class RemoveContact(ContactOperation):
    def __init__(
            self, book, yes_no_validator, check_user_in_the_list, return_contact):
        super().__init__(
            book=book, yes_no_validator=yes_no_validator,
            check_user_in_the_list=check_user_in_the_list,
            return_contact=return_contact)

    def operation(self):
        user_input: str = input(
            "What user do you want to remove? ").capitalize()
        checker: bool = self.check_user_in_the_list.logic_check_operation(
            user_input)
        if checker:
            user_answer: str = input("Are you sure? y/n ")
            user_answer: str = self.yes_no_validator.validation(user_answer)
            if user_answer:
                check_answer: str = self.return_contact.logic_check_operation(
                    user_input)
                self.book.list_of_contacts.remove(check_answer)
            else:
                return
