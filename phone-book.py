from abc import ABC, abstractmethod


class Operations(ABC):
    @abstractmethod
    def execute(self):
        pass


class Checking(Operations):
    def exexute(self):
        if not self.phone_book:
            print("Your phone book is empty")
            while True:
                user_answer: str = input(
                    "Do you want to add contact? (y) yes (n) no: ")
                if not user_answer:
                    print("It's empty. Try again")
                elif user_answer.lower() == "y":
                    self.add_contact()
                    break
                elif user_answer.lower() == "n":
                    break
                else:
                    print("You have wrong type of data or word! Try again.")
        else:
            for i in self.phone_book:
                print(i)


class Adding(Operations):
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
        # name: str = name.capitalize()
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
        # self.phone_book.append(name)


class Editing(Operations):
    def execute(self):
        while True:
            user_answer = input("What contact do you want to change? ")
            if not user_answer:
                print("It's empty. Try again")
            elif user_answer in self.phone_book:
                self.phone_book  # Continue working on edititng


class Deleting(Operations):
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


class Clearing(Operations):
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


class Comunication:
    def __init__(self, text="Welcome! This is phone book app! You can press q to quit.",
                 text2="Bye"):
        self.text = text
        self.text2 = text2

    def say_hi(self):
        print(self.text)

    def say_bye(self):
        print(self.text2)


class PhoneBook:
    def __init__(self, ui: Comunication):
        self.phone_book = []
        self.ui = ui

    def user_wish(self):
        operations = {1: self.check_contacts,
                      2: self.add_contact,
                      3: self.edit_contatct,
                      4: self.delete_contact,
                      5: self.clear_phone_book,
                      }
        print("\n Avaibal operations:")
        for keys, func in operations.items():
            print(f"{keys}: {func.__name__}")
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
                operations[user_answer]()
            else:
                print("Only numbers!")
                continue
            print("\n Avaibal operations:")
            for keys, func in operations.items():
                print(f"{keys}: {func.__name__}")

    def user_wish(self):
        operations = {1: self.check_contacts,
                      2: self.add_contact,
                      3: self.edit_contatct,
                      4: self.delete_contact,
                      5: self.clear_phone_book,
                      }
        print("\n Avaibal operations:")
        for keys, func in operations.items():
            print(f"{keys}: {func.__name__}")
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
                operations[user_answer]()
            else:
                print("Only numbers!")
                continue
            print("\n Avaibal operations:")
            for keys, func in operations.items():
                print(f"{keys}: {func.__name__}")


def main():
    while True:
        ui = Comunication()
        app = PhoneBook(ui)
        app.run()


if __name__ == "__main__":
    main()
