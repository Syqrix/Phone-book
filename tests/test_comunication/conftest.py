from main import Comunication
import pytest


@pytest.fixture
def obj():
    return Comunication()
