# This module allows to check data
import sys
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validation(self, user_input, string=None):
        pass


class CheckerYesOrNo(Validator):
    @staticmethod
    def validation(user_input: str) -> bool:
        while True:
            if not user_input:
                print("Type something!")
            elif user_input.lower() in ["yes", "ye", "y"]:
                return True
            elif user_input.lower() in ["no", "n", "q"]:
                return False
            else:
                print("Wrong type of data, try again!")


class ChekerForInt(Validator):
    @staticmethod
    def validation(user_answer: str, string: int) -> int:
        while True:
            if not user_answer:
                print("It's empty please try enter something!")
                user_answer = input(string)
                continue
            elif user_answer.lower() == "q":
                sys.exit()
            elif user_answer.isalpha():
                print("Only numbers!")
                user_answer = input(string)
                continue
            else:
                return int(user_answer)


class CheckEmptyImportantData(Validator):
    @staticmethod
    def validation(user_input: str, string: str) -> bool:
        while True:
            if not user_input:
                print("This valuse should'nt be empty!, please enter something.")
                user_input = input(string)
                continue
            else:
                return user_input


class NumberValidator(Validator):
    @staticmethod
    def validation(user_input: str, string: str) -> str:
        while True:
            if not user_input:
                print("This valuse should'nt be empty!, please enter something.")
                user_input = input(string).capitalize()
                continue
            elif not user_input.isdigit():
                print("Only numbers!")
                user_input = input(string).capitalize()
                continue
            elif len(user_input) != 11:
                print("Wrong len of number should be 11!")
                user_input = input(string).capitalize()
                continue
            elif user_input[0] not in ["7", "8"]:
                print("Wrong region.")
                user_input = input(string)
                continue
            else:
                return user_input
