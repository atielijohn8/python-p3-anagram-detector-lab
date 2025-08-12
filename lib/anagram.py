class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        matches = []
        for w in words:
            
            if w.lower() != self.word and sorted(w.lower()) == sorted(self.word):
                matches.append(w)
        return matches
