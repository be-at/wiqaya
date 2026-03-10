from pathlib import Path
from .utils import remove_tashkeel
import re

DATA_DIR = Path(__file__).parent / "data"

class Wiqaya:
    def __init__(self, lang: str):
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
        return any(p.match(word) for p in self._patterns)

    def _is_bad(self, word: str) -> bool:
        return word in self.WORDS or self._matches_any_pattern(word)

    def is_profane(self, text) -> bool:
        return any(self._is_bad(w) for w in self._process(text))

    def get_profane_words(self, text) -> list[str]:
        return [w for w in self._process(text) if self._is_bad(w)]

    def censor(self, text: str, char: str = "*") -> str:
        for word in self._process(text):
            if self._is_bad(word):
                text = text.replace(word, char * len(word))
        return text

    def _process(self, text: str) -> list[str]:
        # حذف التشكيل من الكلمات العربية لتجنب التحايل
        if self.lang == "ar":
            text = remove_tashkeel(text)
        return text.lower().split()