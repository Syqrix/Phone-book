# This window for main content of my app
from ui import Comunication
from models import Contact, PhoneBook
from logic import ContactOperations, PhoneBookOperations, Menu
from utilities.validators import Checker


class App:
    def __init__(self, ui: Comunication, menu: Menu):
        self.ui = ui
        self.menu = menu

    def run(self):
        while True:
            self.ui.say_hi()
            self.menu.user_wish()
            self.ui.say_bye()
            break


def main():

    ui = Comunication()
    checker = Checker()
    menu = Menu(checker)
    app = App(ui, menu)
    app.run()


if __name__ == "__main__":
    main()
