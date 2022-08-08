
"""
German test - uses german-nouns pypi
"""

from german_nouns.lookup import Nouns
nouns = Nouns()
word = nouns["Aussicht"]
print(word[0]["flexion"]["akkusativ plural"], word[0]["genus"])

"""
French test - 
"""
