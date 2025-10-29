# This block of code allows to comunicate with user
from time import sleep


class Comunication:
    def say_hi(self) -> None:
        print("Welcome! This is phone book app!")

    def say_bye(self) -> None:
        print("Bye, thank you for using.")
        print("Exiting...")
        sleep(2)
