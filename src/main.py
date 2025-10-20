# This window for main content of my app
from ui import SayHi, SayBye
from logic import ContactOperation, Menu, PhoneBookOperation, DataManager
from logic import CheckFolder, CheckPhoneBook, ClearPhoneBook, ExitPhoneBook
from logic import ChooseOperation, CreateContact, CheckContact, EditContact
from logic import RemoveContact
from logic import SaveData, LoadData, LoadDataFromJson, SaveDataToJson
from models import PhoneBook
from utilities import Check, ChekerForInt, CheckerYesOrNo, CheckEmptyImportantData
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
    book = PhoneBook()
    int_validator = ChekerForInt()
    yes_no_validator = CheckerYesOrNo()
    empty_check_validator = CheckEmptyImportantData()
    number_validator = NumberValidator()
    choose_user_wish = ChooseOperation()
    check_duplicat_names = CheckDublicatNames()
    check_dublicat_number = CheckDublicatNumber()
    check_user_in_the_list = CheckUserInTheList()
    return_contact_index = ReturnContactIndex()
    return_contact = ReturnContact()
    abstract_logic_check = Check(book)
    abstract_data_manager = DataManager(book)
    abstract_load_data = LoadData(book)
    abstract_save_data = SaveData(book)
    save_json_data = SaveDataToJson()
    load_json_data = LoadDataFromJson()
    say_hi = SayHi()
    say_bye = SayBye()
    check_folder = CheckFolder()
    abstract_phone_operation = PhoneBookOperation(
        book, yes_no_validator, say_bye, save_json_data)
    abstract_contact_operation = ContactOperation(
        empty_check_validator, number_validator, int_validator, yes_no_validator,
        check_duplicat_names, check_dublicat_number, check_user_in_the_list,
        return_contact_index, return_contact)
    create_contact = CreateContact()
    check_contact = CheckContact()
    edit_contact = EditContact()
    remove_contact = RemoveContact()
    check_phone_book = CheckPhoneBook()
    clear_phone_book = ClearPhoneBook()
    exit_phone_book = ExitPhoneBook()
    menu = Menu(
        int_validator, check_phone_book, clear_phone_book, exit_phone_book,
        create_contact, check_contact, edit_contact, remove_contact)
    app = App(
        say_hi, say_bye, choose_user_wish, check_folder,
        load_json_data, save_json_data)
    app.run()


if __name__ == "__main__":
    main()
