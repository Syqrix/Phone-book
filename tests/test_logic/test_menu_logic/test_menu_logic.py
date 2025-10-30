import pytest


class TestMenuLogic:
    class TestMenu:
        @staticmethod
        def test_menu(fake_menu, monkeypatch, capsys):
            inputs = iter(["10", "1", "q"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            with pytest.raises(SystemExit):
                fake_menu.choose_the_operation()
            captured = capsys.readouterr()
            assert "Not in avaibale range, try again." in captured.out
