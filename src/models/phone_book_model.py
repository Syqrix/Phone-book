# This is block of code for initialization of our data
from dataclasses import dataclass, field
from models import Contact


@dataclass
class PhoneBook:
    list_of_contacts: list[Contact] = field(default_factory=list)
