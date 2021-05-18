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

    def test_extract_place_ou_se_trouve(self):
        parser = Parser()
        result = parser.search_3("Bonjour est-ce que je pourrais savoir ou se trouve la mairie de la ciotat qui se trouve près de Marseille")
        assert result == "la mairie de la ciotat"

