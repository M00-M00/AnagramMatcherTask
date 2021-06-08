import argparse
from anagram_matcher import AnagramMatcher


parser = argparse.ArgumentParser()

parser.add_argument('-A', "--anagram", type= str)
parser.add_argument('-E', '--encoded_messages', nargs='+')
parser.add_argument('-W', '--wordlist', type=str)
args = parser.parse_args()

anagram = args.anagram
encoded_messages= args.encoded_messages
wordlist_filepath = args.wordlist

print(anagram)

"""
if __name__ == "__main__":
    self = AnagramMatcher(wordlist_filepath, anagram, encoded_messages) """