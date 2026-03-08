import re


TASHKEEL = re.compile(r'[\u0610-\u061A\u064B-\u065F]')

# remove tashkeel from arabic
def remove_tashkeel(text: str) -> str:
    if not TASHKEEL.search(text):
        return text
    return TASHKEEL.sub('', text)