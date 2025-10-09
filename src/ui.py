# This block of code allows to comunicate with user

class Comunication:
    def __init__(self,
                 hi_words="Welcome! This is phone book app! You can press q to quit.",
                 bye_words="Bye"):
        self._hi_words: str = hi_words
        self._bye_words: str = bye_words

    def say_hi(self) -> str:
        print(self._hi_words)

    def say_bye(self) -> str:
        print(self._bye_words)
