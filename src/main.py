from ui import Comunication
from models import Contact, PhoneBook
from logic import ContactOperations, PhoneBookOperations
from validators import Checker


class App:
    def __init__(self, ui: Comunication):
        self.ui = ui

    def run(self):
        while True:
            self.ui.say_hi()
            self.ui.say_bye()
            break


def main():
    ui = Comunication()
    Contact()
    PhoneBook()
    app = App(ui)
    app.run()


if __name__ == "__main__":
    main()
