from  pathlib import Path
from .utils import remove_tashkeel


DATA_DIR = Path(__file__).parent.parent.parent / "data"

class Wiqaya:
    def __init__(self, lang: str):
        self.lang = lang

        try:
            with open(f"{DATA_DIR}/{self.lang}.txt", "r", encoding="utf-8") as f:
                self.WORDS = set(line.strip() for line in f)

        except FileNotFoundError:
            raise ValueError(f"Language '{self.lang}' not supported")

    def is_profane(self, text) -> bool:
        words = self._process(text)
        return any(word in self.WORDS for word in words)

    def get_profane_words(self, text) -> list[str]:
        words = self._process(text)
        return [word for word in words if word in self.WORDS]

    def censor(self, text: str, char: str = "*") -> str:
        words = self._process(text)
        for word in words:
            if word in self.WORDS:
                text = text.replace(word, char * len(word))
        return text

    def _process(self, text: str) -> list[str]:
        if self.lang == "ar":
            text = remove_tashkeel(text)
        return text.lower().split()


