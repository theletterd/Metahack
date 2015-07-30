import random
import collections
import re


BANNED_PATTERN = "\[|\]|\(|\)|\""


class HackathonIdeaGenerator(object):

    def __init__(self, filename):
        self.filename = filename
        self.words = collections.defaultdict(list)
        self.populate_dictionary(filename)

    def get_hackathon_idea(self):
        hackathon_idea = []
        current_word = self._get_next_word("'")
        while(current_word and current_word != "'" and len(hackathon_idea) < 15):
            hackathon_idea.append(current_word)
            current_word = self._get_next_word(current_word)

        return u" ".join(hackathon_idea)
    
    def add_new_idea(self, idea):
        if not idea:
            return
        
        with open(self.filename, 'a') as outfile:
            outfile.write(u'{idea}\n'.format(idea=idea))

        self._add_idea(idea)

    def _get_next_word(self, current_word):
        potential_next_words = self.words.get(current_word)
        if potential_next_words:
            return potential_next_words[random.randint(0, len(potential_next_words) - 1)][1]
        return None

    def _add_words(self, key, value):
        if not re.search(BANNED_PATTERN, key):
            if not re.search(BANNED_PATTERN, value[0]) \
                    and not re.search(BANNED_PATTERN, value[1]):
                self.words[key.lower()].append((value[0].lower(), value[1].lower()))
   
    def _add_idea(self, idea):
        word_chain = idea.split()
        if len(word_chain) > 2:
            # Add first and last tuples in sentence to dict.
            self._add_words(
                "'", 
                ("'", word_chain[0])
            )
            self._add_words(
                word_chain[len(word_chain)-1], 
                ("'", "'")
            )

            for j in range(0, len(word_chain)-1):
                self._add_words(
                    word_chain[j], 
                    (word_chain[j], word_chain[j+1])
                )

    def populate_dictionary(self, filename):
        with open(filename, 'r') as infile:
            for line in infile:
              self._add_idea(line) 
