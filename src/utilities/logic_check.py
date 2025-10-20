# This module uses for checkng logic of the app
from abc import ABC, abstractmethod


class Check(ABC):
    def __init__(self, book):
        self.book = book

    @abstractmethod
    def logic_check_operation(self, user_data):
        pass


class CheckUserInTheList(Check):
    def logic_check_operation(self, user_input: str) -> bool:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == user_input:
                return True
            else:
                continue
        return False


class ReturnContact(Check):
    def logic_check_operation(self, user_input: str) -> object:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == user_input:
                return contact
            else:
                continue


class ReturnContactIndex(Check):
    def logic_check_operation(self, user_input: str) -> int:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == user_input:
                index_of_contact = self.book.list_of_contacts.index(contact)
                return index_of_contact
            else:
                continue


class CheckDublicatNumber(Check):
    def logic_check_operation(self, phone_number: str) -> str:
        for contact in self.book.list_of_contacts:
            if contact.phone_number == phone_number:
                print("You already have this number in your phone book")
                return False
            else:
                continue
        return "+" + phone_number


class CheckDublicatNames(Check):
    def logic_check_operation(self, name: str) -> str:
        for contact in self.book.list_of_contacts:
            if contact.contact_name == name:
                print("There is same name already, try another one!")
                return False
            else:
                continue
        return name
