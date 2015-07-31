import random
import collections
import re


BANNED_PATTERN = "\[|\]|\(|\)|\""
START_WORD = 'startword'
END_WORD = 'endword'


class HackathonIdeaGenerator(object):

    def __init__(self, training_file, bestof_file):
        self.training_file = training_file
        self.bestof_file = bestof_file
        self.words = collections.defaultdict(list)
        self.populate_dictionary(training_file)

    def get_hackathon_idea(self):
        for _ in xrange(3):
            idea = self._get_hackathon_idea()
            if len(idea.split()) > 1:
                return idea
        return idea

    def _get_hackathon_idea(self):
        hackathon_idea = []
        current_word = self._get_next_word(START_WORD)
        while(current_word and current_word != END_WORD and len(hackathon_idea) < 25):
            hackathon_idea.append(current_word)
            current_word = self._get_next_word(current_word)

        return u" ".join(hackathon_idea).capitalize()

    def save_idea_to_file(self, idea, filename):
        with open(filename, 'a+') as outfile:
            outfile.write(u'{idea}\n'.format(idea=idea))

    def save_to_bestof(self, idea):
        self.save_idea_to_file(idea, self.bestof_file)

    def get_bestof_ideas(self):
        with open(self.bestof_file, 'r') as f:
            ideas = f.readlines()
        return ideas

    def add_new_idea(self, idea):
        if not idea:
            return

        self.save_idea_to_file(idea, self.training_file)
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

    def clean_line(self, line):
        for character in "?":
            line = line.replace(character, '')

        return line

    def _add_idea(self, idea):
        idea = self.clean_line(idea)
        word_chain = idea.split()
        if len(word_chain) > 5:
            # Add first and last tuples in sentence to dict.
            self._add_words(
                START_WORD,
                (START_WORD, word_chain[0])
            )
            self._add_words(
                word_chain[len(word_chain)-1],
                (END_WORD, END_WORD)
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
