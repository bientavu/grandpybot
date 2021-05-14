from grandpy.parser import Parser

class TestParser:
    def test_remove_all_accents_from_sentence(self):
        parser = Parser()
        result = parser.remove_all_accents("test btv")
        assert result == "test btv"

