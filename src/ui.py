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
