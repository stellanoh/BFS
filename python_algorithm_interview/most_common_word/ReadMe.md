# 가장 흔한 단어
- 리트코드 819번 참조
  - https://leetcode.com/problems/most-common-word
- 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자를 구분하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
- 정답은 소문자로 출력되어야 한다.
- 주어지는 문단의 길이는 최소 1, 최대 1000자이다.
- 문단은 영문자, 띄어쓰기 ' ' , "!?',;." 등이 포함된다.
- 금지된 단어 배열 크기는 0에서 100 이하 이다
- 금지된 단어의 길이는 1에서 10자이며, 소문자이다.

---
### 예제 1
- 입력
```text
  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
```
- 출력
  - "ball"

### 예제 2
- 입력
```text
paragraph = "a.", banned = []
```
- 출력
  - "a"

---
### 풀이방법
- 리스트 컴프리핸션 + Counter 객체 사용
- paragraph 전처리 작업은 정규식 표현을 활용할 수 있음
  - [^\w] 단어 문자가 아니면
  - `re.sub(r'[^\w], ' ', paragraph)` -> 단어 문자가 아니면 공백으로 치환
- 리스트 컴프리핸션을 활용해, paragraph를 돌며 문자를 소문자로 바꾸고, banned에 포함되어 있으면 리스트로 포함시키 않게 만듬
  - `if word not in banned`
- Counter 객체를 사용해 각 단어의 갯수를 count해서 저장후, most_common 함수가 most에서 least 순으로 저장된다는 걸 활용해 1번째 내용물을 빼온다.