from grandpy.parser import Parser

class TestParser:

    def test_remove_all_accents_from_sentence(self):
        parser = Parser()
        result = parser.remove_all_accents("où é")
        assert result == "ou e"

    def test_remove_all_apostrophe_from_sentence(self):
        parser = Parser()
        result = parser.remove_all_apostrophe("palais de l'elysée")
        assert result == "palais de lelysée"

    def test_remove_all_dashes_from_sentence(self):
        parser = Parser()
        result = parser.remove_all_dashes("Notre-Dame de Paris")
        assert result == "Notre Dame de Paris"

    def test_all_letters_in_lower(self):
        parser = Parser()
        result = parser.all_letters_in_lowercase("La MaiRiE De La CiotAt")
        assert result == "la mairie de la ciotat"

    def test_extract_place_ou_est(self):
        parser = Parser()
        result = parser.extract_place("Bonjour ou est Notre Dame de Paris ?")
        assert result == "Notre Dame de Paris "

    def test_extract_place_ou_se_trouve(self):
        parser = Parser()
        result = parser.extract_place("Bonjour ou se trouve la mairie de la ciotat ?")
        assert result == "la mairie de la ciotat "

    def test_extract_place_ou_se_situe(self):
        parser = Parser()
        result = parser.extract_place("Bonjour ou se situe le port du havre ?")
        assert result == "le port du havre "

    def test_parser_execute(self):
        parser = Parser()
        sentence = "Bonjour, où se situe Notre-Dames-des-L'andes ?"
        result  = parser.execute_parser(sentence)
        assert result == "notre dames des landes "

