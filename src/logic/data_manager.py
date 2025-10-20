# This module uses for save data of our contacts
import csv
import json
from dataclasses import asdict
from pathlib import Path
from models import Contact
from abc import ABC, abstractmethod


class DataManager(ABC):

    def __init__(self, book):
        self.path_of_folder = Path("/data")
        self.path_of_text_data = Path("/data/data.txt")
        self.path_of_json_data = Path("/data/data.json")
        self.path_of_csv_data = Path("/data/data.csv")
        self.book = book
        self.json_template = '{"Contacts": []}'

    @abstractmethod
    def operation(self):
        pass


class CheckFolder(DataManager):
    def operation(self):
        if not self.path_of_folder.exists():
            self.path_of_folder.mkdir()


class SaveData(ABC):
    def __init__(self, book):
        self.path_of_folder = Path("/data")
        self.path_of_text_data = Path("/data/data.txt")
        self.path_of_json_data = Path("/data/data.json")
        self.path_of_csv_data = Path("/data/data.csv")
        self.book = book
        self.json_template = '{"Contacts": []}'

    @abstractmethod
    def save_data(self):
        pass


class SaveDataToTxt(SaveData):
    def save_data(self):
        with open(self.path_of_text_data, "w") as file:
            for contact in self.book.list_of_contacts:
                file.write(
                    f"{contact.contact_name}, {contact.phone_number}\n")


class SaveDataToJson(SaveData):
    def save_data(self):
        with open(self.path_of_json_data, "w", encoding="utf-8") as file:
            data = {"contacts": [{"name": contact.contact_name,
                    "phone_number": contact.phone_number
                                  } for contact in self.book.list_of_contacts]}
            json.dump(data, file, indent=4)


class SaveDataToCsv(SaveData):
    def save_data_to_csv(self):
        with open(self.path_of_csv_data, "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone_number"])
            writer.writeheader()
            data = [{"name": contact.contact_name,
                     "phone_number": contact.phone_number
                     } for contact in self.book.list_of_contacts]
            writer.writerows(data)


class LoadData(ABC):
    def __init__(self, book):
        self.path_of_folder = Path("/data")
        self.path_of_text_data = Path("/data/data.txt")
        self.path_of_json_data = Path("/data/data.json")
        self.path_of_csv_data = Path("/data/data.csv")
        self.book = book
        self.json_template = '{"Contacts": []}'

    @abstractmethod
    def load_data(self):
        pass


class LoadDataFromTxt(LoadData):
    def load_data(self):
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


class LoadDataFromJson(LoadData):

    def load_data(self):
        if not self.path_of_json_data.exists():
            self.path_of_json_data.touch()
        if self.path_of_json_data.stat().st_size == 0:
            return

        with open(self.path_of_json_data, "r", encoding="utf-8") as file:
            data = json.load(file)
            data = data["contacts"]
            for obj in data:
                new_contact = Contact(contact_name=obj.get(
                    "name"), phone_number=obj.get("phone_number"))
                self.book.list_of_contacts.append(new_contact)


class LoadDataFromCsv(LoadData):
    def load_data(self):
        if not self.path_of_csv_data.exists():
            self.path_of_csv_data.touch()

        with open(self.path_of_csv_data, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_contact = Contact(
                    contact_name=row['name'], phone_number=row["phone_number"])
                self.book.list_of_contacts.append(new_contact)
