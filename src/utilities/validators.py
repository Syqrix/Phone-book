# This module allows to check data
import sys


class Validators:
    @staticmethod
    def check_y_n_validator(user_answer: str, text_input: str) -> bool:
        while True:
            if not user_answer:
                print("Type something!")
                user_answer = input(text_input)
                continue
            elif user_answer.lower() in ["yes", "ye", "y"]:
                return True
            elif user_answer.lower() in ["no", "n", "q"]:
                return False
            else:
                print("Wrong type of data, try again!")
                user_answer = input(text_input)
                continue

    @staticmethod
    def check_int_validator(user_answer: str, text_input: str) -> int:
        while True:
            if not user_answer:
                print("It's empty please try enter something!")
                user_answer = input(text_input)
                continue
            elif user_answer.lower() == "q":
                print("Exiting...")
                sys.exit()
            elif user_answer.isalpha():
                print("Only numbers!")
                user_answer = input(text_input)
                continue
            else:
                return int(user_answer)

    @staticmethod
    def check_empty_important_data_validator(user_input: str, text_input: str) -> str:
        while True:
            if not user_input:
                print(
                    "This valuse should'nt be empty!, please enter something.")
                user_input = input(text_input).capitalize()
                continue
            else:
                return user_input

    @staticmethod
    def check_phone_number_validator(user_input: str, text_input: str) -> str:
        while True:
            if not user_input:
                print(
                    "This valuse should'nt be empty!, please enter something.")
                user_input = input(text_input)
                continue
            elif not user_input.isdigit():
                print("Only numbers!")
                user_input = input(text_input)
                continue
            elif len(user_input) != 11:
                print("Wrong len of number should be 11!")
                user_input = input(text_input)
                continue
            elif user_input[0] not in ["7", "8"]:
                print("Wrong region.")
                user_input = input(text_input)
                continue
            else:
                return user_input
