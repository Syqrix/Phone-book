import csv
from dataclasses import asdict


class DataManager:
    def __init__(self, book):
        self.book = book

    def save_contacts_to_csv(self):
        with open("data/contacts.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["contact_name", "phone_number"])
            writer.writeheader()
            for contact in self.book.list_of_contacts:
                writer.writerow(asdict(contact))
