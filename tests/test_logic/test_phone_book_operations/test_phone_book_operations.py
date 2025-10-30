import pytest
import os


class TestPhoneBookOperations:
    class TestShowContact:
        @staticmethod
        def test_show_false(fake_phone_book_operation_empty, capsys):
            fake_phone_book_operation_empty.show_contacts()
            captured = capsys.readouterr()
            assert "There is nothing in the phone book." in captured.out

        @staticmethod
        def test_show_true(fake_phone_book_operation_with_data, capsys):
            fake_phone_book_operation_with_data.show_contacts()
            captured = capsys.readouterr()
            assert "Fake name | +70000000000" in captured.out

    class TestClearPhoneBook:
        @staticmethod
        def test_clear_phone_book_none(
                fake_phone_book_operation_empty, capsys, monkeypatch):
            inputs = iter(["N"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            result = fake_phone_book_operation_empty.clear_phone_book()
            captured = capsys.readouterr()
            assert result is None

        @staticmethod
        def test_clear_phone_book_true(
                fake_phone_book_operation_with_data, capsys, monkeypatch):
            inputs = iter(["Y"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_phone_book_operation_with_data.show_contacts()
            fake_phone_book_operation_with_data.clear_phone_book()
            fake_phone_book_operation_with_data.show_contacts()
            captured = capsys.readouterr()
            assert "Fake name | +70000000000" in captured.out
            assert "Phone book has been cleared!" in captured.out
            assert "There is nothing in the phone book." in captured.out
