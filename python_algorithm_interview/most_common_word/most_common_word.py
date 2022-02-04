import collections
import re
from typing import List


def most_common_word(self, paragraph: str, banned: List[str]) -> str:
    # paragraph preprocessing
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    # check the most frequent one
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]