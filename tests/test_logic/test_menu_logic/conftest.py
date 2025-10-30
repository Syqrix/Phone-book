import pytest
from logic import PhoneBookOperations, SaveDataToJson, ContactOperations, Menu
from models import PhoneBook
from ui.comunication import Comunication
from utilities.logic_check import CheckLogic


@pytest.fixture
def fake_check_logic(fake_phone_book):
    return CheckLogic(fake_phone_book)


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
def fake_contact_operations(fake_phone_book, fake_check_logic):
    return ContactOperations(fake_phone_book, fake_check_logic)


@pytest.fixture
def fake_phone_book_operation_empty(fake_phone_book, fake_ui, fake_save_json):
    return PhoneBookOperations(fake_phone_book, fake_ui, fake_save_json)


@pytest.fixture
def fake_menu(fake_phone_book_operation_empty, fake_contact_operations):
    return Menu(fake_phone_book_operation_empty, fake_contact_operations)
