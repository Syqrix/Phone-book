from abc import ABC, abstractmethod
import json
import csv


class Operations(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Checking(Operations):
    def __init__(self, phone_book: list):
        self.phone_book = phone_book

    def execute(self):
        if not self.phone_book:
            print("Your phone book is empty")
        else:
            for i in self.phone_book:
                print(i)

    def name(self):
        return "Check the phone book"


class Adding(Operations):
    def __init__(self, phone_book: list):
        self.phone_book = phone_book

    def execute(self):
        while True:
            name: str = input("Name: ")
            if not name:
                print("Please enter the name.")
                continue
            if name.isdigit():
                print("Please enter the letters!")
                continue
            else:
                break
        name: str = name.capitalize()
        # while True:
        #     try:
        #         phone = int(input("Please enter your number only 11 numbers"))
        #     except TypeError:
        #         print("Wrong type again!")
        #         continue
        #     if len(str(phone)) != 11:
        #         print("Number more or less than 11. Please try again")
        #         continue
        #     else:
        #         break
        # phone = "+" + str(phone)
        self.phone_book.append(name)

    def name(self):
        return "Add contact"


class Editing(Operations):
    def __init__(self, phone_book: list):
        self.phone_book = phone_book

    def execute(self):
        while True:
            user_answer = input("What contact do you want to change? ")
            if not user_answer:
                print("It's empty. Try again")
            elif user_answer in self.phone_book:
                self.phone_book  # Continue working on edititng

    def name(self):
        return "Edit a contact"


class Deleting(Operations):
    def __init__(self, phone_book: list):
        self.phone_book = phone_book

    def execute(self):
        while True:
            user_answer = input(
                "What user do you want to delete? ").capitalize()
            if not user_answer:
                print("It's empty try again.")
                continue
            else:
                break
        if user_answer in self.phone_book:
            self.phone_book.remove(user_answer)
            print(f"User: {user_answer} has been deleted.")
        else:
            print(f"There is no the user: {user_answer} in your phone book")
            type_of_variations = []
            for i in range(len(self.phone_book)):
                if self.phone_book[i][0:len(user_answer)] == user_answer[0:]:
                    type_of_variations.append(self.phone_book[i])
                else:
                    continue
                i = 0
                while True:
                    try:
                        checker = input(
                            "Did you mean {}.y-yes n-no: ".format(type_of_variations[i]))
                    except IndexError:
                        print("There are not options anymore!")
                        break
                    if checker.lower() == "y":
                        self.phone_book.remove(type_of_variations[i])
                        print(
                            f"User: {type_of_variations[i]} has been deleted.")
                        break
                    elif checker.lower() == "n":
                        i += 1
                    else:
                        print("Wrong type of data!")

    def name(self):
        return "Delete a contact"


class Clearing(Operations):
    def __init__(self, phone_book: list):
        self.phone_book = phone_book

    def execute(self):
        if not self.phone_book:
            print("Nothing to clear. It's empty!")
        else:
            while True:
                user_answer = input(
                    "Do you want clear the phone book? (y) yes (n) no: ")
                if not user_answer:
                    print("It's empty try again!")
                elif user_answer.lower() == "y":
                    self.phone_book.clear()
                    print("Phone book has been cleared!")
                    break
                elif user_answer.lower() == "n":
                    break
                else:
                    print("Error: Wrong type of data or words. Try again")

    def name(self):
        return "Clear the phone book"


class Comunication:
    def __init__(self, text="Welcome! This is phone book app! You can press q to quit.",
                 text2="Bye"):
        self._text: str = text
        self._text2: str = text2

    def say_hi(self):
        print(self._text)

    def say_bye(self):
        print(self._text2)


class PhoneBook:
    def __init__(self):
        self.phone_book = []

    def user_wish(self):
        operations = {1: Checking(self.phone_book),
                      2: Adding(self.phone_book),
                      3: Editing(self.phone_book),
                      4: Deleting(self.phone_book),
                      5: Clearing(self.phone_book),
                      }
        print("\n Avaibal operations:")
        for keys, func in operations.items():
            print(f"{keys}: {func.name()}")
        while True:
            user_answer_str = input(
                "What kind of operation do you want to use? ")
            if not user_answer_str:
                print("It's empty please try enter something!")
                continue
            if user_answer_str.lower() == "q":
                return None
            if user_answer_str.isdigit():
                user_answer = int(user_answer_str)
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
        self. proces = proces

    def run(self):
        self.ui.say_hi()
        self.proces.user_wish()
        self.ui.say_bye()


def main():
    while True:
        ui = Comunication()
        proces = PhoneBook()
        app = App(ui, proces)
        app.run()


if __name__ == "__main__":
    main()
