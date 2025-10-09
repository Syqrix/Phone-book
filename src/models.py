from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    company: str
    phone_number: str
    notes: str
    contact: str


@dataclass
class PhoneBook:
    phone_book: list
