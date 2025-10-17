from main import Comunication
import pytest


class TestComunication:
    @pytest.fixture
    def obj(self):
        return Comunication()

    def test_hi(self, obj, capsys):
        obj.say_hi()
        output = capsys.readouterr().out
        assert "Welcome! This is phone book app! You can press q to quit." in output
