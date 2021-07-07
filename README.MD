##AnagramMatcher
AnagramMatcher finds anagrams of a sentence/ combination of words in a wordlist and matches their md5 hashes to provided ones in order to unlock a secret message.
Installation
Use the package manager pip to install the required packages
`` $ pip install -r requirements.txt ``
	

###RUN:

`` $ python main.py -W path/to/wordlist.txt -A "anagram" -E encoded messages  ``

-W - path to the word list 
-A - anagram, string in " "  (e.g )
-E - encoded messages, separated by a spacebar (e.g  12j3i2 1232ik 12323)


###DEMO:
`` run example.py  ``
for demo
demo is already setup to find answers for anagram "poultry outwits ants" with reference md5_hashes ["e4820b45d2277f3844eac66c903e84be", "23170acc097c24edb98fc5488ab033fe", "665e5bcb0c20062fe8abaaf4628bb154"]. 
It can be started by simply running
$ python challenge.py 
	

###TESTS:

Test can be run by
`` $ pytest ``
	





License
MIT
