# This is block of code for initialization of our contact data
from dataclasses import dataclass


@dataclass
class Contact:
    contact_name: str
    phone_number: str
