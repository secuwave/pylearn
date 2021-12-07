# 정규표현

## 정규표현

정규표현식/정규식/Regular Expression

* 특정한 문자열 집합을 표현하는 형식 언어
* 여러 텍스트 편집기, OS 유틸리티, 프로그래밍 언어 등에서 문자열데이터 검색, 치환, 추출을 위해 지원
  * Snort, Yara, IOC 탐지패턴 표현 옵션
  * Perl, Python, Rubi 등 스크립트 언어에 내장
  * Ultra Editor, Notepad++, Visual Studio Code 등 다양한 편집기 검색 옵션 포함

## 참고자료
* 초보자를 위한 정규표현식 가이드
  * [https://www.slideshare.net/ibare/ss-39274621](https://www.slideshare.net/ibare/ss-39274621)
  * 정규표현 기초를 잘 설명

(다른 잘 설명한 사이트가 많으니, 필요 시 정규표현 기본을 검색 권장)

## 기본 설명
pdf: [OpenbaseSecurity_LearningScript_04.pdf](OpenbaseSecurity_LearningScript_04.pdf)

## character class

| 정규표현식  | 설명                                     | 등가의 다른 정규표현식     |
|------------|------------------------------------------|---------------------------|
| .          | 모든 문자, 개행문자(new line)을 제외하고.  | [^\n]                     |
| [...]      | 괄호 안에 있는 문자 중 아무거나 하나       |   |
| [^...]     | 괄호 안에 있는 문자가 아닌 것 아무거나 하나 |   |
| \w         | word 구성 문자                            | [a-zA-Z0-9_], [[:alnum:]_] |
| \W         | word 구성 문자가 아닌 것                  | [^a-zA-Z0-9_], [^[:alnum:]_] |
| \s         | 스페이스 구성 문자 중 하나                | [ \t\n\r\f\v], [[:space:]] |
| \S         | 스페이스 구성 문자가 아닌 것              | [^ \t\n\r\f\v], [^[:space:]]|
| \d         | 숫자 1개                                 | [0-9], [[:digit:]] |
| \D         | 숫자가 아닌 문자                          | [^0-9], [^[:digit:]] |

##### 참고: [[:class:]]: alnum, alpha, ascii, blank, cntrl, digit, graph, lower, print, punct, space, upper, xdigit

## quantifier (수량자)

| 정규표현식  | 설명                                     | 등가의 다른 정규표현식     |
|------------|------------------------------------------|---------------------------|
| {n, m}     | n개 이상 m개 이하      | |
| {n, }      | n개 이상               | |
| {n}        | n개                   | {n, n} |
| ?          | 0개 또는 1개, 없거나 1개가 있음            | {0, 1} |
| *          | 0개 이상, 없거나 무제한 있을 수 있음       | {0, } |
| +          | 1개 이상, 하나이상 무제한 있을 수 있음     | {1, } |
| {}?        | {n, m}, {n, }, {n}의 non-greedy match.   | |
| ??         | ?의 non-greedy match.  | |
| *?         | *의 non-greedy match.  | |
| +?         | +의 non-greedy match.  | |

## Anchor
패턴이 일치해야 하는 시작위치/종료위치/경계 조건을 지정한다.

| 정규표현식  | 설명               |
|------------|--------------------|
| ^          | 문자열의 시작       |
| $          | 문자열의 끝, 줄끝   |
| \b         | word boundary, 단어의 경계 즉, \w와 \W사이|
| \B         | word boundary가 아닌 경우 |

## modifier(Options)

패턴을 매칭시키는 옵션을 조정한다. 
적용 형태는 다음 중 하나인 경우가 많다:
* (?i)xxxx, (?mi)xxxx
* /xxxx/i, /xxxx/m

| modifier      | 설명                       |
|---------------|----------------------------|
| i             | 대소문자 구분 안함          |
| s(singleline) | .에 new line이 포함됨, ^과 $이 \n을 무시 |
| m(multiline)  | ^과 $을 내부 \n(newline)에 적용 |


## 실습1

text
```
Navigate to the home dashboard
The home dashboard is the first dashboard a user sees when they sign in to Grafana. You can also navigate to the home dashboard manually.
---------> click
Hover your cursor over the Dashboards (four squares) icon.
Click Home.
Set the home dashboard for the server
Users with the Grafana Server Admin flag on their account or access to the configuration file can define a JSON file to use as the home dashboard for all users on the server.
button
[Optional] Convert an existing dashboard into a JSON file
Navigate to the page of the dashboard you want to use as the home dashboard.
Click the Share dashboard icon next to the dashboard title.
In the Export tab, click Save to file. Grafana converts the dashboard to a JSON file and saves it locally.
click
cl
ick this button
```

test1: s 옵션 적용에 따른 매칭 범위 확대
```
dashboard.*with vs (?s)dashboard.*with
```

test2:
```
(?si)cli.*ck vs (?si)cli.*?ck vs (?si)^cli.*ck
```

test3: .*을 .*?으로 바꾸면서 non-greedy가 돼서 일치하는 최소 범위를 매칭으로 결정한다.
```
(?si)cli.*button vs (?si)cli.*?button
```

## 실습2: grouping
대칭하는 문자열 찾기

매칭되는 파트 일부를 괄호로 묶으면 뒤에서 \1, \2... \n(괄호 순서대로)으로 재참조 할 수 있다. 정규표현에서 grouping이라고 한다.

text
```
김 윤 김
kim youn kim
kim youn gil
정 은 정
Rebert R Robert
Rebert R Brown
정 은 미
333-384657489-333
22323-343543-22323
22323-343543-22320
```

test1: 단순 대칭 검색
```
(.+).*\1
```

test2: 구분자(스페이스 또는 -)까지 맞춰서 대칭인 경우를 찾음
```
test: (.+)([\s-]).+\2\1
```

### 실습3: look ahead/behind
text1
```
1000원
2000원
3000원
5000원
10000원
10000W
```

test1: look ahead, 뒤쪽에 만족하는 조건이 있으면 그 앞 부분을 matching한다. 숫자 뒤에 "원"이 오면 그 앞부분 숫자를 매칭하여 금액으로 인지한다.
```
 \d+(?=원)
```

text2
```
1: $600.4
2: $10.25
3: $47.33
4: $112.34
```

test2: look behind, 앞쪽에 만족하는 조건이 있으면 그 뒤 부분을 matching한다. 숫자와 점(달러는 소수 포함)으로 된 패턴 앞에 "$"이 오면 달러 금액으로 인지한다.
```
(?<=\$)[0-9.]+
```
## 기타 실습용 HTML 파일

(내려받아서 notepad로 열어 놓고 실습에 사용)

[sample.html](sample.html)

test: html에서 링크를 거는 태그인 ```<a href=...>``` 부분을 찾아서 모든 링크를 검색하려고 할 때, ```<a href=.+>``` 정규표현을 사용하면, 태그 하나가 여러 줄에 걸쳐 있는 경우 찾을 수 없으므로 ```(?s)<a href=.+>```와 같이 s옵션을 붙인다. 그런데, .+는 GREEDY-MATCHING을 하기 때문에 ">"이 나올때 까지 최대한 매칭을 시켜서 여러개 태그가 매칭범위에 포함 된다. 따라서 최소 점위만 매칭되도록 아래와 같은 정규표현을 사용한다.
```
(?s)<a href=.+?>
```
<meta>