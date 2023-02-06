from collections import Counter

all_words = []

def anagram_count(name, words):
    count = 0
    name = Counter(list(name))
    for word in all_words:
        if Counter(list(word)) == name:
            count += 1
    return count
