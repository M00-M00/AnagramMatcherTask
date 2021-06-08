from collections import Counter, defaultdict
import string
import random
import re
import json
import os
import hashlib

ENCODED_MESSAGES =  ["e4820b45d2277f3844eac66c903e84be", "23170acc097c24edb98fc5488ab033fe", "665e5bcb0c20062fe8abaaf4628bb154"]

PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class AnagramMatcher(): 

    def __init__(self, wordlist_name : str, anagram: str, encoded_messages: list):
        

        self.anagram = anagram.replace(" ", "")
        self.unique_letters = self.get_unique_letters(anagram)
        self.hashed_letters = dict(zip(self.unique_letters, PRIME_NUMBERS[:len(self.unique_letters)]))
        print(self.unique_letters)
        self.target_hash = self.string_to_hash(self.anagram)
        print(self.target_hash)
        self.two_primes = []
        self.two_primes_mult = defaultdict(list)
        self.wordlist = []
        self.anagrams = defaultdict(list)
        self.sentences = []
        self.hash_l = {}
        self.load_words(wordlist_name)
        self.group_anagrams(self.wordlist)
        self.group_words_by_prime() 
        self.answers = []
        self.md5_hashes = []
        self.secret_messages = []

        self.find_sentences()
        for sentence in self.sentences:
            self.compare_md5_hash(sentence, encoded_messages)
        print(self.secret_messages)
         

    
    def group_words_by_prime(self):
        word_list = {"group": [],  "histogram": [], "hash": [], "word": [], "index": []}
        ind = 0
        for word in self.wordlist:
            word_list["index"].append(ind)
            word_list["word"].append(word)
            group = self.anagrams[word]
            word_list["group"].append(group)
            word_hash = self.string_to_hash(word)
            print(word_hash)
            word_list["hash"].append(word_hash)
            self.hash_l[word_hash] = ind
            ind += 1
        self.word_list = word_list    
        return self.word_list



    def find_sentences(self):
        hash_set = set(self.word_list["hash"])
        hash_set2 = set(self.word_list["hash"])
        hash_list = self.word_list["hash"]
        hash_list.sort()
        while len(hash_set) > 0:
            h1 = hash_set.pop()
            h_2_3 = self.target_hash / h1
            print(h_2_3)
            if h_2_3 in hash_set or h_2_3 / int(h_2_3) == 1:
                self.two_primes.append(int(h_2_3))
        while len(hash_set2) > 0:
            h1 = hash_set2.pop()
            h2_near = self.target_hash / h1
            #print("h2_near:" + str(h2_near))
            h2_r = (min(self.hash_l, key=lambda x:abs(x-h2_near))) 
            h2_range = hash_list.index(h2_r)
            h2_set = set(list(hash_set2)[:h2_range])
            for h2 in h2_set:
                h2_3 = h1 * h2
                if int(h2_3) in self.two_primes:
                    h3 = self.target_hash / h2_3
                    print(str(self.target_hash) + "----" +  str(h1 * h2 * h3))
                    answer = [h1,h2,h3]
                    self.answers.append(answer)
        for hl in self.answers:
            self.sentences.append([self.hash_to_sentences(hl)])
        return self.sentences

        


    def hash_to_sentences(self, hash_list):
        names = []
        for h in hash_list:
            names.append(self.word_list["word"][self.hash_l[(int(h))]])
        return(names[0] + " " + names[1] + " " + names[2])



    def load_words(self, textfile):
        print ("Loading word list from file...")
        # 'with' can automate finish 'open' and 'close' file
        unused_letters_regex = self.regex_unused_letters(self.unique_letters)
        print(unused_letters_regex)
        with open(textfile) as f:
            # fetch one line each time, include '\n'
            for line in f:
                # strip '\n', then append it to wordlist
                w = line.rstrip('\n')
                word = (re.sub(r'[^a-z]',r'',w))
                search = re.search(unused_letters_regex, word)
                if search == None:
                    #print(word)
                    self.wordlist.append(word)
            print( " ", len(self.wordlist), "words loaded.")
            self.wordlist = list(dict.fromkeys(self.wordlist))
            new_list = []
            for w in self.wordlist:
                print(w)
                if self.compare_histograms(self.string_to_histogram(self.anagram), self.string_to_histogram(w)) != False: 
                    new_list.append(w)
            #print '\n'.join(wordlist)
            self.wordlist =  new_list
        return self.wordlist


    def compare_md5_hash(self, sentence: list, reference: list):
        result = hashlib.md5(sentence[0].encode())
        # printing the equivalent hexadecimal value.
        print("The hexadecimal equivalent of hash is : ", end ="")
        print(result.hexdigest())
        self.md5_hashes.append(result.hexdigest())
        if result.hexdigest() in reference:
            print("MATCH")
            print(sentence, result.hexdigest(), reference)
            self.secret_messages.append([sentence, result.hexdigest(), reference])
        else:
            print(result.hexdigest() + "NOPE!")

    def group_anagrams(self, wordlist):
        for word in wordlist:
            self.anagrams["". join(sorted(word))].append(word)
        return self.anagrams


    @staticmethod
    def get_unique_letters(phrase):
        no_spaces = phrase.replace(" ", "")
        letters =  list({l  for l in no_spaces})
        return letters         


    def string_to_histogram(self, string):
        string.replace(" ", "")
        histogram = dict(Counter(string).items())
        formatted_histogram = {}
        target_letters = self.unique_letters
        for l in target_letters:
            if l in histogram:
                formatted_histogram[l] = histogram[l]
            else:
                formatted_histogram[l] = 0
        return formatted_histogram

    @staticmethod
    def create_default_dict(length: int) -> dict:
        words = defaultdict(dict)
        for n in range(1,length + 1):
            words[n] = defaultdict(list)
        return words



    def string_to_hash(self, word: str):
        word.replace(" ", "")
        prime_numbers = self.hashed_letters
        value = 1  
        for n in word:
            value *=  prime_numbers[n] 
        return value



    @staticmethod
    def compare_histograms(l1, l2):
        l1 = list(l1.values())
        l2 = list(l2.values())
        if False in [l1[n] >= l2[n] for n in range(len(l1))]:
            return False


    @staticmethod
    def regex_unused_letters(unique_letters):
        letters = ALPHABET.copy()
        for l in unique_letters:

            letters.remove(l)
        string_letters = str(letters).replace("'", "").replace(", ", "")    
        return string_letters




if __name__ == "__main__":
    self = AnagramMatcher("wordlist.txt", "poultry outwits ants", ENCODED_MESSAGES)



 

