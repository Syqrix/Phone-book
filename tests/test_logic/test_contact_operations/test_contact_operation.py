class TestContactsOperations:
    class TestCreate:
        @staticmethod
        def test_create(
                fake_contact_operations_empty, monkeypatch, capsys):
            inputs = iter(["fake text", "70000000000"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_contact_operations_empty.create()
            captured = capsys.readouterr()
            assert "User: Fake text has been created!" in captured.out

    class TestCheck:
        @staticmethod
        def test_check_true(
                fake_contact_operations_with_data, monkeypatch, capsys):
            inputs = iter(["true text"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_contact_operations_with_data.check_contact()
            captured = capsys.readouterr()
            assert "User: True text is in the phone book!" in captured.out

        @staticmethod
        def test_check_false(
                fake_contact_operations_with_data, monkeypatch, capsys):
            inputs = iter(["false text"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_contact_operations_with_data.check_contact()
            captured = capsys.readouterr()
            assert "User: False text is not in the phone book!" in captured.out

    class TestEdit:
        @staticmethod
        def test_edit_name(
                fake_contact_operations_with_data, monkeypatch, capsys):
            inputs = iter(
                ["true text", "1",  "new true name", "new true name"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_contact_operations_with_data.edit()
            fake_contact_operations_with_data.check_contact()
            captured = capsys.readouterr()
            assert "User: New true name is in the phone book!" in captured.out

        @staticmethod
        def test_edit_phone_number(
                fake_contact_operations_with_data,
                fake_phone_book_operation_empty, monkeypatch):
            fake_phone_book_operation_empty.show_contacts()
            assert "True name | +70000000000"
            inputs = iter(
                ["true text", "2",  "71111111111"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_contact_operations_with_data.edit()
            fake_phone_book_operation_empty.show_contacts()
            assert "True name | +71111111111"

    class TestRemove:
        @staticmethod
        def test_remove(
                fake_contact_operations_with_data,
                fake_phone_book_operation_empty, monkeypatch, capsys):
            fake_phone_book_operation_empty.show_contacts()
            inputs = iter(
                ["true text", "Y"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_contact_operations_with_data.remove()
            fake_phone_book_operation_empty.show_contacts()
            captured = capsys.readouterr()
            assert "There is nothing in the phone book." in captured.out
