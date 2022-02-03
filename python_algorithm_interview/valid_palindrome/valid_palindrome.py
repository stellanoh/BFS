import collections
from typing import Deque
import re

def is_palindrome_list(self, s: str) -> bool:
    # 리스트로 해결하는 방법
    strs = []
    # 영문자, 숫자만 리스트에 소문자로 변환 후 append
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 판별, O(N^2)
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome_deque(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    # O(N)
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def is_palindrome_slicing(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 필요 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]