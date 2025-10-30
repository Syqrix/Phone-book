# This module uses for checkng logic of the app
from typing import Union


class CheckLogic:
    def __init__(self, book):
        self.book = book

    def check_user_in_the_list(self,  target: str) -> bool:
        self.book.list_of_contacts.sort(
            key=lambda contact: contact.contact_name)
        low: int = 0
        high: int = len(self.book.list_of_contacts) - 1
        mid: int = (low + high) / 2
        while low <= high:
            mid = (low + high) // 2
            if self.book.list_of_contacts[mid].contact_name < target:
                low = mid + 1
            elif self.book.list_of_contacts[mid].contact_name > target:
                high = mid - 1
            else:
                return True
        return False

    def return_contact(self, target: str) -> Union[object, None]:
        self.book.list_of_contacts.sort(
            key=lambda contact: contact.contact_name)
        low: int = 0
        high: int = len(self.book.list_of_contacts) - 1
        mid: int = (low + high) / 2
        while low <= high:
            mid = (low + high) // 2
            if self.book.list_of_contacts[mid].contact_name < target:
                low = mid + 1
            elif self.book.list_of_contacts[mid].contact_name > target:
                high = mid - 1
            else:
                return target
        return None

    def return_contact_index(self, target: str) -> Union[int, None]:
        self.book.list_of_contacts.sort(
            key=lambda contact: contact.contact_name)
        low: int = 0
        high: int = len(self.book.list_of_contacts) - 1
        mid: int = (low + high) / 2
        while low <= high:
            mid = (low + high) // 2
            if self.book.list_of_contacts[mid].contact_name < target:
                low = mid + 1
            elif self.book.list_of_contacts[mid].contact_name > target:
                high = mid - 1
            else:
                return mid
        return None

    def check_dublicat_number(self, target: str) -> Union[str, bool]:
        self.book.list_of_contacts.sort(
            key=lambda contact: contact.phone_number)
        low: int = 0
        high: int = len(self.book.list_of_contacts) - 1
        mid: int = (low + high) / 2
        while low <= high:
            mid = (low + high) // 2
            if self.book.list_of_contacts[mid].phone_number[1:] < target:
                low = mid + 1
            elif self.book.list_of_contacts[mid].phone_number[1:] > target:
                high = mid - 1
            else:
                print("You already have this number! try another one")
                return False
        return "+" + target

    def check_dublicat_names(self, target: str) -> str:
        self.book.list_of_contacts.sort(
            key=lambda contact: contact.contact_name)
        low: int = 0
        high: int = len(self.book.list_of_contacts) - 1
        mid: int = (low + high) / 2
        while low <= high:
            mid = (low + high) // 2
            if self.book.list_of_contacts[mid].contact_name < target:
                low = mid + 1
            elif self.book.list_of_contacts[mid].contact_name > target:
                high = mid - 1
            else:
                print(
                    "You already have such user in your phone book! Try another one")
                return False
        return target
