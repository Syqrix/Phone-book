# This is block of code for initialization of our data
from dataclasses import dataclass


@dataclass
class Contact:
    contact_name: str
    company: str
    phone_number: str
    notes: str
