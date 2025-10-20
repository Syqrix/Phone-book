# This block of code allows to comunicate with user
from time import sleep
from abc import ABC, abstractmethod


class Comunication(ABC):
    def __init__(self,
                 hi_words="Welcome! This is phone book app!",
                 bye_words="Bye, thank you for using."):
        self._hi_words: str = hi_words
        self._bye_words: str = bye_words

    @abstractmethod
    def say(self):
        pass


class SayHi(Comunication):
    def say(self) -> str:
        print(self._hi_words)


class SayBye(Comunication):
    def say(self) -> str:
        print(self._bye_words)
        print("Exiting...")
        sleep(2)
