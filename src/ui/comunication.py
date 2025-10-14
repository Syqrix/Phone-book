# This block of code allows to comunicate with user
from time import sleep


class Comunication:
    def __init__(self,
                 hi_words="Welcome! This is phone book app!",
                 bye_words="Bye, thank you for using."):
        self._hi_words: str = hi_words
        self._bye_words: str = bye_words

    def say_hi(self) -> str:
        print(self._hi_words)

    def say_bye(self) -> str:
        print(self._bye_words)
        print("Exiting...")
        sleep(2)
