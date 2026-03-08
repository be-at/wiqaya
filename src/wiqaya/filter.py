from  pathlib import Path



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
        words = text.lower().split()
        return any(word in self.WORDS for word in words)

    def get_profane_words(self, text) -> list[str]:
        words = text.lower().split()
        return [word for word in words if word in self.WORDS]



t = Wiqaya("ar").get_profane_words("اهلا بك يا بزاز")
print(t)