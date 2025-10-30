import pytest
from logic import ContactOperations, PhoneBookOperations, SaveDataToJson
from models import PhoneBook, Contact
from utilities.logic_check import CheckLogic
from ui.comunication import Comunication


@pytest.fixture
def fake_save_json():
    return SaveDataToJson(fake_phone_book)


@pytest.fixture
def fake_ui():
    return Comunication()


@pytest.fixture
def fake_check_logic(fake_phone_book):
    return CheckLogic(fake_phone_book)


@pytest.fixture
def fake_phone_book():
    return PhoneBook()


@pytest.fixture
def fake_contact_operations_empty(fake_phone_book, fake_check_logic):
    return ContactOperations(fake_phone_book, fake_check_logic)


@pytest.fixture
def fake_contact_operations_with_data(fake_phone_book, fake_check_logic):
    new_contact = Contact("True text", "+70000000000")
    fake_phone_book.list_of_contacts.append(new_contact)
    return ContactOperations(fake_phone_book, fake_check_logic)


@pytest.fixture
def fake_phone_book_operation_empty(fake_phone_book, fake_ui, fake_save_json):
    return PhoneBookOperations(fake_phone_book, fake_ui, fake_save_json)
