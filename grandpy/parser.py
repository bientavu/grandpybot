import unidecode
import re

class Parser:
    
    def remove_all_accents(self, sentence):
        """Removes all accents contained in the sentence"""
        unaccented_string = unidecode.unidecode(sentence)
        return unaccented_string

    def remove_all_apostrophe(self, sentence):
        """Removes all apostrophe contained in the sentence"""
        original_string = sentence
        new_string = original_string.replace("'", "")
        return new_string

    def remove_all_dashes(self, sentence):
        """Removes all dashes contained in the sentence"""
        original_string = sentence
        new_string = original_string.replace("-", " ")
        return new_string

    def all_letters_in_lowercase(self, sentence):
        """All letters are put in lowercase"""
        original_string = sentence
        new_string = original_string.lower()
        return new_string

    def extract_place(self, sentence):
        """
        Takes the 5 next words after the keyword
        to extract what the users want to search
        """
        words_to_find = r"(?<=ou est )[^,.!?\n]+|" \
        r"(?<=ou se trouve )[^,.!?\n]+|" \
        r"(?<=ou se situe )[^,.!?\n]+|" \
        r"(?<=adresse )[^,.!?\n]+|"
        found_words = re.findall(words_to_find, sentence, flags=re.IGNORECASE)
        found_words_in_string = ''.join(found_words)
        return found_words_in_string

    def execute_parser(self, sentence):
        """Execute all the parser methods above"""
        parser = Parser()
        remove_all_accents = parser.remove_all_accents(sentence)
        remove_all_apostrophe = parser.remove_all_apostrophe(remove_all_accents)
        remove_all_dashes = parser.remove_all_dashes(remove_all_apostrophe)
        all_letters_in_lowercase = parser.all_letters_in_lowercase(remove_all_dashes)
        extract_place = parser.extract_place(all_letters_in_lowercase)
        return extract_place

