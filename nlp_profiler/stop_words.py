import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nlp_profiler.constants import NaN

nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))


### Stop words
def gather_stop_words(text: str) -> list:
    if not isinstance(text, str):
        return []

    word_tokens = word_tokenize(text)
    found_stop_words = [word for _, word in enumerate(word_tokens)
                        if word in STOP_WORDS]
    return found_stop_words


def count_stop_words(text: str) -> int:
    if not isinstance(text, str):
        return NaN

    return len(gather_stop_words(text))
