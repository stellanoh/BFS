# 유효한 팰린드롬
- 리트코드 125번 참조
  - https://leetcode.com/problems/valid-palindrome
  
- 주어진 문자열이 팰린드롬인지 확인하라. **대소문자를 구분하지 않으며, 영문자와 숫자만을 대상**으로 한다.
- isPalindrome 함수를 구현해야 하며 string s가 파라미터로 주어짐
- s의 길이는 1이상 2*10^5 
- 리턴 타입은 bool 타입
- empty string도 palindrome

### 팰린드롬이란?
- 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 or 문장

---
### 예제 1
- 입력
  - "A man, a plan, a canal: Panama"
- 출력
  - true
  
### 예제 2
- 입력
  - "race a car"
- 출력 
  - false

---
### 풀이방법1
- 리스트
  - 리스트로 선언후, 영문자,숫자만 리스트에 append
  - 리스트의 마지막과 처음의 값이 일치하지 않으면 false 리턴
  - pop(0)함수의 경우 O(n) 시간 소요, n번 반복하므로 총 O(n^2) 
