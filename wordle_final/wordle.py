from enum import Enum
import random
from valid_words import valid_words


class Game:
    def __init__(self):
        self.set_correct_word()
        self._dictionary = WordleWord("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # ---------------------------
    # Correct Word
    # ---------------------------
    def set_correct_word(self):
        self._correct_word = WordleWord(random.choice(valid_words))

    def get_correct_word(self):
        return self._correct_word

    # ---------------------------
    # Used by UI (Pygame)
    # Submit a guess from user input
    # ---------------------------
    def submit_guess(self, guess_string: str):
        guess_string = guess_string.lower()

        # Validate guess
        if guess_string not in valid_words:
            return None, False   # invalid guess

        # Convert to WordleWord
        user_guess = WordleWord(guess_string)

        # Compare words
        won = user_guess.compare_word(self._correct_word)

        # Update global letter dictionary statuses
        self.set_letter_dictionary_status(user_guess)

        return user_guess, won

    # ---------------------------
    # Update letter dictionary
    # ---------------------------
    def set_letter_dictionary_status(self, user_guess):
        for letter in user_guess.letter_list:
            for dictionary_letter in self._dictionary.letter_list:
                if dictionary_letter.name == letter.name:
                    # Only upgrade the status (CORRECT > WRONG_PLACEMENT > GUESSED)
                    if dictionary_letter.status.value < letter.status.value:
                        dictionary_letter.status = letter.status
                    break


# ======================================================================
# WORD
# ======================================================================

class WordleWord:
    def __init__(self, word_string):
        self.word_string = word_string
        word_string_up = self.word_string.upper()
        self.letter_list = []

        pos = 0
        for char in list(word_string_up):
            pos += 1
            self.letter_list.append(WordleLetter(char, pos))

    def __str__(self):
        return "".join([str(letter) for letter in self.letter_list])

    # Compare this guess to the correct word
    def compare_word(self, correct_word):
        correct_word.reset_word()

        # Pass 1: exact matches
        for i, letter in enumerate(self.letter_list):
            if letter.name == correct_word.get_letter_position(i).name:
                letter.status = Status.CORRECT
                correct_word.get_letter_position(i).status = Status.CORRECT

        # Pass 2: wrong-place matches
        for letter in self.letter_list:
            correct_word.set_wrong_place_status(letter)

        # Pass 3: remaining = guessed but wrong
        for letter in self.letter_list:
            if letter.status == Status.NOT_GUESSED:
                letter.status = Status.GUESSED

        # Check win
        return all(letter.status == Status.CORRECT for letter in self.letter_list)

    def set_wrong_place_status(self, letter):
        for cw_letter in self.letter_list:
            if (cw_letter.status == Status.NOT_GUESSED and 
                letter.status == Status.NOT_GUESSED and 
                letter.name == cw_letter.name):

                cw_letter.status = Status.WRONG_PLACEMENT
                letter.status = Status.WRONG_PLACEMENT

    def get_letter_position(self, position):
        return self.letter_list[position]

    def reset_word(self):
        for letter in self.letter_list:
            letter.status = Status.NOT_GUESSED


# ======================================================================
# LETTER
# ======================================================================

class WordleLetter:
    def __init__(self, name: str, position: int):
        self._name = name
        self._position = position
        self._status = Status.NOT_GUESSED

    def __str__(self):
        return f"{self._position} - {self._name} - {self._status.name}\n"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new):
        self._name = new

    @property
    def position(self):
        return self._position

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, stat):
        self._status = stat


# ======================================================================
# STATUS ENUM
# ======================================================================

class Status(Enum):
    NOT_GUESSED = 1
    GUESSED = 2
    WRONG_PLACEMENT = 3
    CORRECT = 4