# This block of code allows to check what we need fast
class Checker:
    @staticmethod
    def checker_yes_or_no(self, user_input) -> str:
        while True:
            if not user_input:
                print("Type something!")
            elif user_input.lower() in ["yes", "ye", "y"]:
                return True
            elif user_input.lower() in ["no", "n", "q"]:
                return
            else:
                print("Wrong type of data, try again!")

    @staticmethod
    def checker_for_int(self, user_answer) -> int:
        while True:
            if not user_answer:
                print("It's empty please try enter something!")
                continue
            elif user_answer.lower() == "q":
                return None
            elif user_answer.isalpha():
                print("Only numbers!")
                continue
            else:
                return int(user_answer)
