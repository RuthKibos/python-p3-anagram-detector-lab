# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, find_anagrams):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)
        # Initialize an empty list to store matches
        matches = []
        # Iterate over the list of possible anagrams
        for candidate in find_anagrams:
            # Sort the letters of the candidate word
            sorted_candidate = sorted(candidate)
            # Compare the sorted letters
            if sorted_word == sorted_candidate:
                # If they match, add to matches
                matches.append(candidate)
        return matches