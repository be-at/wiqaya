# Wiqaya 🛡️

A Python library for multilingual profanity detection and filtering. It identifies and censors offensive or abusive words across multiple languages.

## Installation

```bash
pip install wiqaya
```

## Usage

```python
from wiqaya import Wiqaya

w = Wiqaya(lang="ar")

w.is_profane("هذا نص عادي")       # False
w.is_profane("نص يحتوي شتيمة")    # True

w.get_profane_words("نص فيه كلمة سيئة")  # ['كلمة سيئة']
```

## Supported Languages

| Code | Language | Code | Language | Code | Language |
|------|----------|------|----------|------|----------|
| af | Afrikaans | am | Amharic | ar | العربية |
| az | Azerbaijani | be | Belarusian | bg | Bulgarian |
| ca | Catalan | ceb | Cebuano | cs | Czech |
| cy | Welsh | da | Danish | de | German |
| dz | Dzongkha | el | Greek | en | English |
| eo | Esperanto | es | Spanish | et | Estonian |
| eu | Basque | fa | Persian | fi | Finnish |
| fil | Filipino | fr | French | gd | Scottish Gaelic |
| gl | Galician | hi | Hindi | hr | Croatian |
| hu | Hungarian | hy | Armenian | id | Indonesian |
| is | Icelandic | it | Italian | ja | Japanese |
| kab | Kabyle | kh | Khmer | ko | Korean |
| la | Latin | lt | Lithuanian | lv | Latvian |
| mi | Maori | mk | Macedonian | ml | Malayalam |
| mn | Mongolian | mr | Marathi | ms | Malay |
| mt | Maltese | my | Burmese | nl | Dutch |
| no | Norwegian | pih | Norfuk | piy | Picard |
| pl | Polish | pt | Portuguese | ro | Romanian |
| rop | Kriol | ru | Russian | sk | Slovak |
| sl | Slovenian | sm | Samoan | sq | Albanian |
| sr | Serbian | sv | Swedish | ta | Tamil |
| te | Telugu | tet | Tetum | th | Thai |
| tlh | Klingon | to | Tongan | tr | Turkish |
| uk | Ukrainian | uz | Uzbek | vi | Vietnamese |
| yid | Yiddish | zh | Chinese | zu | Zulu |