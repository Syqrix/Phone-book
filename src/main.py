# This window for main content of my app
from ui.comunication import Comunication
from logic import PhoneBookOperations, Menu
from logic import ContactOperations
from logic import LoadDataFromJson, SaveDataToJson, DataManager
from models import PhoneBook
from utilities import CheckLogic


class App:
    def __init__(
        self,
        ui: Comunication,
        menu: Menu,
        check_folder: DataManager,
        load_json_data: LoadDataFromJson,
        save_json_data: SaveDataToJson,
    ):
        self.ui = ui
        self.menu = menu
        self.check_folder = check_folder
        self.load_json_data = load_json_data
        self.save_json_data = save_json_data

    def run(self):
        while True:
            self.check_folder.check_folder()
            self.load_json_data.load_data()
            self.ui.say_hi()
            self.menu.choose_the_operation()
            self.save_json_data.save_data()
            self.ui.say_bye()


def main():
    # --- Phone book ---
    book = PhoneBook()

    # --- Comunication ---
    ui = Comunication()

    # --- Check logic utilit ---
    check_logic = CheckLogic(book)

    # --- Data ---
    save_json_data = SaveDataToJson(book)
    load_json_data = LoadDataFromJson(book)
    check_folder = DataManager()

    # ---Phone book operatins---
    phone_book_operations = PhoneBookOperations(book, ui, save_json_data)

    # --- Operations ---
    contact_operations = ContactOperations(book, check_logic)
    # --- Menu ---
    menu = Menu(phone_book_operations, contact_operations)

    # --- Main App ---
    app = App(ui, menu, check_folder, load_json_data, save_json_data)
    app.run()


if __name__ == "__main__":
    main()
