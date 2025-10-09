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
