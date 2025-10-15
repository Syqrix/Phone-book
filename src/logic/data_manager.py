import csv
import json
from dataclasses import asdict
from pathlib import Path
from models import Contact


class DataManager:

    def __init__(self, book):
        self.path_of_folder = Path(
            "/media/edward/Data/Projects/vsCode_projects/Python/phone-book/data")
        self.path_of_text_data = Path(
            "/media/edward/Data/Projects/vsCode_projects/Python/phone-book/data/data.txt")
        self.path_of_json_data = Path(
            "/media/edward/Data/Projects/vsCode_projects/Python/phone-book/data/data.json")
        self.path_of_csv_data = Path(
            "/media/edward/Data/Projects/vsCode_projects/Python/phone-book/data/data.csv")
        self.book = book

    def check_folder(self):
        if not self.path_of_folder.exists():
            self.path_of_folder.mkdir()

    def save_data_to_txt(self):
        with open(self.path_of_text_data, "w") as file:
            for contact in self.book.list_of_contacts:
                file.write(
                    f"{contact.contact_name}, {contact.phone_number}\n")

    def load_data_from_txt(self):
        self.book.list_of_contacts = []
        if not self.path_of_text_data.exists():
            self.path_of_text_data.touch()

        with open(self.path_of_text_data, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, phone_number = line.split(",")
                    name = name.strip()
                    phone_number = phone_number.strip()

                    contact = Contact(contact_name=name,
                                      phone_number=phone_number)

                    self.book.list_of_contacts.append(contact)
                except ValueError:
                    print("Wrong data")

        for i in self.book.list_of_contacts:
            print(i)
