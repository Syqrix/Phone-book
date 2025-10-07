from abc import ABC, abstractmethod
import json
import csv


class Comunication:
    def __init__(self,
                 text="Welcome! This is phone book app! You can press q to quit.",
                 text2="Bye"):
        self._text: str = text
        self._text2: str = text2

    def say_hi(self) -> str:
        print(self._text)

    def say_bye(self) -> str:
        print(self._text2)


class Contact:
    def __init__(self, first_name: str,
                 last_name: str, company: str,
                 phone_number: str, notes: str, proces: PhoneBook):
        self.first_name: str = first_name
        self.last_name = last_name
        self.company = company
        self.phone_number = phone_number
        self.notes = notes
        self.proces = proces
        self.contact = {}

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


class Checker:

    def checker_yes_or_no(self, user_input):
        while True:
            if not user_input:
                print("Type something!")
            elif user_input.lower() in ["yes", "ye", "y"]:
                return True
            elif user_input.lower() in ["no", "n", "q"]:
                return
            else:
                print("Wrong type of data, try again!")


class PhoneBook:
    def __init__(self, checker: Checker, contact: Contact):
        self.phone_book: list = []
        self.checker = checker
        self.contact = contact

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


class UserWish:

    def user_wish(self):
        operations: dict = {}
        print("\n Avaibal operations:")
        for keys, func in operations.items():
            print(f"{keys}: {func.name()}")
        while True:
            user_answer_str: str = input(
                "What kind of operation do you want to use? ")
            if not user_answer_str:
                print("It's empty please try enter something!")
                continue
            if user_answer_str.lower() == "q":
                return None
            if user_answer_str.isdigit():
                user_answer: int = int(user_answer_str)
                operations[user_answer].execute()
            else:
                print("Only numbers!")
                continue
            print("\n Avaibal operations:")
            for keys, func in operations.items():
                print(f"{keys}: {func.name()}")


class App:
    def __init__(self, ui: Comunication, proces: PhoneBook):
        self.ui = ui
        self.proces = proces

    def run(self):
        self.ui.say_hi()
        self.proces.user_wish()
        self.ui.say_bye()


def main():
    while True:
        ui = Comunication()
        checker = Checker()
        contact = Contact()
        proces = PhoneBook(checker, contact)
        app = App(ui, proces)
        app.run()


if __name__ == "__main__":
    main()
