class TestComunication:
    @staticmethod
    def test_hi(obj, capsys):
        obj.say_hi()
        captured = capsys.readouterr().out
        assert "Welcome! This is phone book app!" in captured

    @staticmethod
    def test_bye(obj, capsys):
        obj.say_bye()
        captured = capsys.readouterr()
        assert "Bye, thank you for using." in captured.out
        assert "Exiting..." in captured.out
