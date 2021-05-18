import unidecode
import re

class Parser:
    def remove_all_accents(self, sentence):
        """Removes all accents contained in the sentence"""
        unaccented_string = unidecode.unidecode(sentence)
        return unaccented_string

    def remove_all_apostrophe(self, sentence):
        original_string = sentence
        new_string = original_string.replace("'", "")
        return new_string

    def extract_place(self, sentence):
        """Takes the 3 next words"""
        string = sentence
        words_to_find = 'Ou se trouve|Ou est|'
        index_number = string.find('Ou se trouve')
        return string[-8:index_number]

    def search(self, sentence):
        word = r"\W*([\w]+)"
        words_to_find = 'ou se trouve|ou est'
        groups = re.search(r'{}\W*{}{}'.format(word*5, 'ou se trouve', word*5), sentence, flags=re.IGNORECASE).groups()
        place_string =  ' '.join(groups[5:])
        return place_string

    def search_2(self, sentence):
        words_to_find = 'ou se trouve|ou est'
        found_words = re.findall(words_to_find, sentence, flags=re.IGNORECASE)
        return found_words

    def search_3(self, sentence):
        return re.findall(r"ou se trouve[a-zA-Z]+", sentence, flags=re.IGNORECASE)

