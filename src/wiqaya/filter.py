from pathlib import Path
from .utils import remove_tashkeel
import re

DATA_DIR = Path(__file__).parent / "data"

class Wiqaya:
    def __init__(self, lang: str):
        """
        Initialize the Wiqaya profanity filter for a given language.

        Loads the word list from a language-specific .txt file in the data directory.
        Entries containing '*' are treated as wildcard patterns and compiled into
        regex objects. Plain entries are stored in a set for O(1) lookup.

        Args:
            lang (str): Language code (e.g., 'ar', 'en'). Must match a filename in data/.
        
        Raises:
            ValueError: If no word list file exists for the given language.
        """
        self.lang = lang
        try:
            with open(f"{DATA_DIR}/{self.lang}.txt", "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            raise ValueError(f"Language '{self.lang}' not supported")

        self.WORDS = set()
        self._patterns = []
        for entry in lines:
            if "*" in entry:
                # Convert wildcard to regex: *word* → .*word.*, word* → word.*
                regex = re.escape(entry).replace(r"\*", ".*")
                self._patterns.append(re.compile(f"^{regex}$"))
            else:
                self.WORDS.add(entry)

    def _matches_any_pattern(self, word: str) -> bool:
        """
        Check whether a word matches any of the compiled wildcard regex patterns.

        Args:
            word (str): The word to test.

        Returns:
            bool: True if the word matches at least one pattern, False otherwise.
        """
        return any(p.match(word) for p in self._patterns)

    def _is_bad(self, word: str) -> bool:
        """
        Determine if a single word is considered profane.

        Checks both the exact-match word set and the wildcard pattern list.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is profane, False otherwise.
        """
        return word in self.WORDS or self._matches_any_pattern(word)

    def is_profane(self, text: str) -> bool:
        """
        Return True if the text contains at least one profane word.

        Args:
            text (str): The input text to scan.

        Returns:
            bool: True if any profane word is found, False otherwise.
        """
        return any(self._is_bad(w) for w in self._process(text))

    def get_profane_words(self, text: str) -> list[str]:
        """
        Extract and return all profane words found in the text.

        Args:
            text (str): The input text to scan.

        Returns:
            list[str]: A list of every word in the text that is considered profane.
        """
        return [w for w in self._process(text) if self._is_bad(w)]

    def censor(self, text: str, char: str = "*") -> str:
        """
        Replace each profane word in the text with a repeated censor character.

        The replacement preserves the original word's length (e.g., 'hell' → '****').

        Args:
            text (str): The input text to censor.
            char (str): The character used for censoring. Defaults to '*'.

        Returns:
            str: The censored version of the input text.
        """
        for word in self._process(text):
            if self._is_bad(word):
                text = text.replace(word, char * len(word))
        return text

    def _process(self, text: str) -> list[str]:
        """
        Normalize and tokenize the input text into a list of words.

        For Arabic text, diacritics (tashkeel) are stripped first to prevent
        users from bypassing the filter by adding vowel marks to profane words.
        The text is then lowercased and split on whitespace.

        Args:
            text (str): The raw input text.

        Returns:
            list[str]: A list of normalized, lowercase tokens.
        """
        if self.lang == "ar":
            text = remove_tashkeel(text)
        return text.lower().split()