from challenge import AnagramMatcher
import unittest

class TestAnagramMatcher(unittest.TestCase):
    pass
    

    def test_compare_md5_hash_pass(self):
        reference = ["8b35bbd7ff2f5dd7c94fffbb1a3512bc"]
        self = AnagramMatcher("test_wordlist.txt", "ty outlaws printouts", reference)
        sentence = ["poultry outwits ants"]
        expected = [sentence, reference[0], reference]
        self.compare_md5_hash(sentence, reference)
        assert self.secret_messages == [expected] 
    

    def test_compare_md5_hash_pass(self):
        reference = ["8b35bbd7ff2f5dd7cfawifjwafwaa3512bc"]
        self = AnagramMatcher("test_wordlist.txt", "ty outlaws printouts", reference)
        sentence = ["poultry outwits ants"]
        expected = [sentence, reference[0], reference]
        self.compare_md5_hash(sentence, reference)
        assert self.secret_messages != [expected] 


    def test_load_words(self):
        reference = ["8b35bbd7ff2f5dd7c94fffbb1a3512bc"]
        self = AnagramMatcher("test_wordlist.txt", "ty outlaws printouts", reference)
        assert len(self.wordlist) == 4


    def test_load_words_regex(self):
        reference = ["8b35bbd7ff2f5dd7c94fffbb1a3512bc"]
        self = AnagramMatcher("test_wordlist.txt", "ty outlaws printouts", reference)
        assert "жest" not in self.wordlist

    def test_load_words_compare_histograms(self):
        reference = ["8b35bbd7ff2f5dd7c94fffbb1a3512bc"]
        self = AnagramMatcher("test_wordlist.txt", "ty outlaws printouts", reference)
        assert "dog" not in self.wordlist

    def test_string_to_hash(self):
        hash_ = AnagramMatcher.string_to_hash("poultry")
        assert hash_ == 510510


    def test_string_to_histogram(self):
        histogram = AnagramMatcher.string_to_histogram("poultry")
        assert histogram == {'p': 1, 'o': 1, 'u': 1, 'l': 1, 't': 1, 'r': 1, 'y': 1, 'w': 0, 'i': 0, 's': 0, 'a': 0, 'n': 0}


    def test_compare_histograms_pass(self):
        h1 = {'p': 1, 'o': 1, 'u': 1, 'l': 1, 't': 1, 'r': 1, 'y': 1, 'w': 0, 'i': 0, 's': 0, 'a': 0, 'n': 0}
        h2 = {'p': 2, 'o': 2, 'u': 2, 'l': 1, 't': 1, 'r': 1, 'y': 1, 'w': 0, 'i': 0, 's': 0, 'a': 0, 'n': 0}
        answer = AnagramMatcher.compare_histograms(h2, h1)
        assert answer == None

    def test_compare_histograms_fail(self):
        h1 = {'p': 1, 'o': 1, 'u': 1, 'l': 1, 't': 1, 'r': 1, 'y': 1, 'w': 0, 'i': 0, 's': 0, 'a': 0, 'n': 0}
        h2 = {'p': 2, 'o': 2, 'u': 2, 'l': 1, 't': 1, 'r': 1, 'y': 1, 'w': 0, 'i': 0, 's': 0, 'a': 0, 'n': 0}
        answer = AnagramMatcher.compare_histograms(h1, h2)
        assert answer == False

    def test_find_sentences(self):
        reference = ["8b35bbd7ff2f5dd7c94fffbb1a3512bc"]
        sentence = ["poultry outwits ants"]
        sentence2 = ["ants poultry outwits"]
        sentence3 = ["outwits poulty ants"]
        self = AnagramMatcher("test_wordlist.txt", "ty outlaws printouts", reference)
        assert sentence in self.sentences
        assert len(self.sentences) == 3

    def test_group_words_by_prime(self):
        self = AnagramMatcher("test_wordlist.txt", "ty outlaws printouts",["8b35bbd7ff2f5dd7c94fffbb1a3512bc"])
        ind = self.word_list["word"].index("ants")
        assert list(self.hash_l.keys())[ind] == AnagramMatcher.string_to_hash("ants")
        assert  AnagramMatcher.string_to_hash("ants") in self.word_list["hash"]
        assert type(self.word_list["index"][ind]) is int


