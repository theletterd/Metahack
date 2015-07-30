import random
import collections
import re


BANNED_PATTERN = "\[|\]|\(|\)|\""


class HackathonIdeaGenerator(object):

    def __init__(self, filename):
        self.words = collections.defaultdict(list)
        self.populate_dictionary(filename)

    def get_hackathon_idea(self):
        hackathon_idea = []
        current_word = self.get_next_word("'")
        while(current_word and current_word != "'"):
            hackathon_idea.append(current_word)
            current_word = self.get_next_word(current_word)

        return u" ".join(hackathon_idea)


    def get_next_word(self, current_word):
        potential_next_words = self.words.get(current_word)
        if potential_next_words:
            return potential_next_words[random.randint(0, len(potential_next_words) - 1)]
        return None

    def add_words(self, key, value):
        if not re.match(BANNED_PATTERN, key) and not re.match(BANNED_PATTERN, value):
            self.words[key.lower()].append(value.lower())

    def populate_dictionary(self, filename):
        with open(filename, 'r') as infile:
            for line in infile:
                word_chain = line.split()
                if len(word_chain) > 1:
                    # Add first and last tuples in sentence to dict.
                    self.add_words("'", word_chain[0])
                    self.add_words(word_chain[len(word_chain)-1], "'")

                    for j in range(0, len(word_chain)-1):
                        self.add_words(word_chain[j], word_chain[j+1])
