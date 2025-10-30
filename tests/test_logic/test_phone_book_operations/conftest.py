import pytest
from logic import PhoneBookOperations, SaveDataToJson
from models import PhoneBook, Contact
from ui.comunication import Comunication


@pytest.fixture
def fake_save_json():
    return SaveDataToJson(fake_phone_book)


@pytest.fixture
def fake_ui():
    return Comunication()


@pytest.fixture
def fake_phone_book():
    return PhoneBook()


@pytest.fixture
def fake_phone_book_operation_with_data(fake_phone_book, fake_ui, fake_save_json):
    new_contact = Contact("Fake name", "+70000000000")
    fake_phone_book.list_of_contacts.append(new_contact)
    return PhoneBookOperations(fake_phone_book, fake_ui, fake_save_json)


@pytest.fixture
def fake_phone_book_operation_empty(fake_phone_book, fake_ui, fake_save_json):
    return PhoneBookOperations(fake_phone_book, fake_ui, fake_save_json)
