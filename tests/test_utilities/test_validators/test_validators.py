import pytest


class TestValidators:
    class TestValidatorYN:
        @staticmethod
        def test_y_n_validator_true(obj):
            result = obj.check_y_n_validator("Y", "Fake text")
            assert result == True

        @staticmethod
        def test_y_n_validator_false(obj):
            result = obj.check_y_n_validator("N", "Fake text")
            assert result == False

        @staticmethod
        def test_y_n_validator_wrong(obj, monkeypatch, capsys):
            inputs = iter(["5", "gjf", "y"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            obj.check_y_n_validator("", "Fake text")
            captured = capsys.readouterr()
            assert "Type something!" in captured.out
            assert "Wrong type of data, try again!" in captured.out

    class TestValidatorInt:
        @staticmethod
        def test_int_validator_true(obj):
            result = obj.check_int_validator("5", "Fake text")
            assert result == 5

        @staticmethod
        def test_int_validator_false(obj, monkeypatch, capsys):
            inputs = iter(["gjhfd", "5"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            result = obj.check_int_validator("", "Fake text")
            captured = capsys.readouterr()
            assert "It's empty please try enter something!" in captured.out
            assert "Only numbers!" in captured.out

        @staticmethod
        def test_int_validator_exit(obj):
            with pytest.raises(SystemExit):
                result = obj.check_int_validator("Q", "Fake text")

    class TestValidatorCheckEmpty:
        @staticmethod
        def test_check_empty(obj, monkeypatch, capsys):
            inputs = iter(["value"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            result = obj.check_empty_important_data_validator("", "Fake text")
            captured = capsys.readouterr()
            assert "This valuse should'nt be empty!, please enter something." in captured.out
            assert result == "Value"

    class TestValidatorPhoneNumber:
        @staticmethod
        def test_validator_phone_number_wrong(obj, monkeypatch, capsys):
            inputs = iter(
                ["gfljkh", "7953454345", "59084943974", "79542357685"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            result = obj.check_phone_number_validator("", "Fake text")
            captured = capsys.readouterr()
            assert "This valuse should'nt be empty!, please enter something." in captured.out
            assert "Only numbers!" in captured.out
            assert "Wrong len of number should be 11!" in captured.out
            assert "Wrong region." in captured.out
            assert result == "79542357685"
