class TestLogicUtilities:
    class TestCheckingUserInTheList:
        @staticmethod
        def test_check_user_in_the_list_false(obj):
            result = obj.check_user_in_the_list("Not right name")
            assert result == False

        @staticmethod
        def test_check_user_in_the_list_true(obj):
            result = obj.check_user_in_the_list("Right name")
            assert result == True

    class TestReturnContact:
        @staticmethod
        def test_return_contact_true(obj):
            object = obj.return_contact("Right name")
            assert object.contact_name == "Right name"

        @staticmethod
        def test_return_contact_false(obj):
            object = obj.return_contact("Not right name")
            assert object == None

    class TestReturnIndex:
        @staticmethod
        def test_index_true(obj):
            result = obj.return_contact_index("Right name")
            assert result == 0

        @staticmethod
        def test_index_false(obj):
            result = obj.return_contact_index("Not right name")
            assert result == None

    class TestDublicatNumber:
        @staticmethod
        def test_dublicat_number_true(obj, capsys):
            result = obj.check_dublicat_number("71234567890")
            captured = capsys.readouterr()
            assert result == False
            assert "You already have this number in your phone book" in captured.out

        @staticmethod
        def test_dublicat_number_false(obj):
            result = obj.check_dublicat_number("70000000000")
            assert result == "+" + "70000000000"

    class TestDublicatName:
        @staticmethod
        def test_dublicat_name_true(obj, capsys):
            result = obj.check_dublicat_names("Right name")
            captured = capsys.readouterr()
            assert result == False
            assert "There is same name already, try another one!" in captured.out

        @staticmethod
        def test_dublicat_name_false(obj):
            result = obj.check_dublicat_names("Not right name")
            assert result == "Not right name"
