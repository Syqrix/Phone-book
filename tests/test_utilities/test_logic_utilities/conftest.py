import pytest
from utilities import CheckLogic
from models import PhoneBook, Contact


@pytest.fixture
def fake_phone_book():
    return PhoneBook()


@pytest.fixture
def obj(fake_phone_book):
    new_contact = Contact("Right name", "+71234567890")
    fake_phone_book.list_of_contacts.append(new_contact)
    return CheckLogic(fake_phone_book)
