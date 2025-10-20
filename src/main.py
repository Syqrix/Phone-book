# This window for main content of my app
from ui import SayHi, SayBye
from logic import CheckFolder, CheckPhoneBook, ClearPhoneBook, ExitPhoneBook
from logic import ChooseOperation, CreateContact, CheckContact, EditContact
from logic import RemoveContact
from logic import LoadDataFromJson, SaveDataToJson
from models import PhoneBook
from utilities import ChekerForInt, CheckerYesOrNo, CheckEmptyImportantData
from utilities import NumberValidator, CheckDublicatNames, CheckDublicatNumber
from utilities import CheckUserInTheList, ReturnContactIndex, ReturnContact


class App:
    def __init__(self, say_hi: SayHi, say_bye: SayBye,
                 choose_user_wish: ChooseOperation, check_folder: CheckFolder,
                 load_json_data: LoadDataFromJson, save_json_data: SaveDataToJson):
        self.say_hi = say_hi
        self.say_bye = say_bye
        self.choose_user_wish = choose_user_wish
        self.check_folder = check_folder
        self.load_json_data = load_json_data
        self.save_json_data = save_json_data

    def run(self):
        while True:
            self.check_folder.operation()
            self.load_json_data.load_data()
            self.say_hi.say()
            self.choose_user_wish.operation()
            self.save_json_data.save_data()
            self.say_bye.say()


def main():
    # --- Phone book ---
    book = PhoneBook()

    # --- Validators ---
    int_validator = ChekerForInt()
    yes_no_validator = CheckerYesOrNo()
    empty_check_validator = CheckEmptyImportantData()
    number_validator = NumberValidator()

    # --- Logic checking ---
    check_duplicat_names = CheckDublicatNames(book)
    check_dublicat_number = CheckDublicatNumber(book)
    check_user_in_the_list = CheckUserInTheList(book)
    return_contact_index = ReturnContactIndex(book)
    return_contact = ReturnContact(book)

    # --- Data ---
    save_json_data = SaveDataToJson(book)
    load_json_data = LoadDataFromJson(book)
    check_folder = CheckFolder(book)

    # --- Ui ---
    say_hi = SayHi()
    say_bye = SayBye()

    # --- Operations ---
    create_contact = CreateContact(
        book, empty_check_validator, number_validator, check_duplicat_names,
        check_dublicat_number)
    check_contact = CheckContact(check_user_in_the_list)
    edit_contact = EditContact(
        book, int_validator, check_user_in_the_list, return_contact_index)
    remove_contact = RemoveContact(
        book, yes_no_validator, check_user_in_the_list, return_contact)
    check_phone_book = CheckPhoneBook(book)
    clear_phone_book = ClearPhoneBook(book, yes_no_validator)
    exit_phone_book = ExitPhoneBook(save_json_data, say_bye)

    choose_user_wish = ChooseOperation(
        int_validator, check_phone_book, clear_phone_book, exit_phone_book,
        create_contact, check_contact, edit_contact, remove_contact)

    # --- Main App ---
    app = App(
        say_hi, say_bye, choose_user_wish, check_folder,
        load_json_data, save_json_data)
    app.run()


if __name__ == "__main__":
    main()
