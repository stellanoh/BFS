# 로그파일 재정렬
- 리트코드 937번 참조
  - https://leetcode.com/problems/reorder-data-in-log-files
- 로그를 재정렬하라. 기준은 아래 참조
  - 로그의 가장 앞 부분을 식벼자
  - 문자로 구성된 로그가 숫자 로그보다 앞에 온다
  - 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로
  - 숫자 로그는 입력 순서대로

---
### 예제 1
- 입력
  - logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
- 출력
  - ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
### 예제 2
- 입력
  - logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
- 출력
  - ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

---
### 풀이방법
- 람다 사용
  - 식별자 다음 요소가 숫자인지 검사에 각각 문자열, 숫자 리스트에 append
  - lambda를 사용해 문자열 리스트 식별자 다음 문자열을 키로 지정 후 오름차순 정렬,
    - 동일한 문장일 경우를 대비해 다음 키는 식별자가 되어 다시 오름차순 정렬
