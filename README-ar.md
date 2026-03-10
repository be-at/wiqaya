[🌐 English](README.md)

# وقاية 🛡️
مكتبة Python للكشف عن الكلمات المسيئة وفلترتها بعدة لغات. تكتشف الكلمات المسيئة وتحجبها.

## التثبيت
```bash
pip install wiqaya
```

## الاستخدام
```python
from wiqaya import Wiqaya

w = Wiqaya(lang="ar")

w.is_profane("حرامي")                        # True
w.is_profane("نص عادي")                      # False
w.get_profane_words("نص فيه حرامي و أطرش")   # ['حرامي', 'أطرش']
```

> [!NOTE]
> تدعم المكتبة إزالة التشكيل تلقائياً عند استخدام اللغة العربية

> [!TIP]
> يدعم المشروع النمط البديل (Wildcard) في قوائم الكلمات — استخدم `*` للتطابق مع أي تسلسل من الأحرف (مثال: `bad*` تطابق `badly`، و`*word*` تطابق أي كلمة تحتوي على `word`)

## اللغات المدعومة 


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