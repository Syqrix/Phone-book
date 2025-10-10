# This is the main logic of our app
import sys


class Menu:
    def __init__(self, checker):
        self.checker = checker

    def user_wish(self):
        operations: dict = {

        }
        print("\n Avaibal operations:")
        for keys, func in operations.items():
            print(f"{keys}: {func.name()}")
        while True:
            user_answer_str: str = input(
                "What kind of operation do you want to use? ")
            user_answer: int = self.checker.checker_yes_or_no(user_answer_str)
            if user_answer in None:
                sys.exit()
            else:
                user_answer
