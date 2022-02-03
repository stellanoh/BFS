def isPalindrome(self, s):
    # 리스트로 해결하는 방법
    strs = []
    # 영문자, 숫자만 리스트에 소문자로 변환 후 append
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True