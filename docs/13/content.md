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
  * 정규식 기초를 잘 설명

* Regular Expression Quick Reference
  * [https://neo.dmcs.pl/pios/Regular_Expression_Quick_Reference.pdf](https://neo.dmcs.pl/pios/Regular_Expression_Quick_Reference.pdf)

  * 정규표현의 basic feature를 요약
  * 위 자료에서 “Character Classes”, “Repetition”, “Anchors” 파트 정도를 익히면 일반적인 정규식 사용 가능
  * 추가로 “Options”, “Grouping” 중요

(다른 잘 설명한 사이트가 많으니, 필요 시 정규식 기본을 검색 권장)


## 실습용 HTML 파일

(내려받아서 notepad로 열어 놓고 실습에 사용)

[sample.html](sample.html)

### character class

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

### quantifier (수량자)

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

### Anchor
패턴이 일치해야 하는 시작위치/종료위치/경계 조건을 지정한다.

| 정규표현식  | 설명               |
|------------|--------------------|
| ^          | 문자열의 시작       |
| $          | 문자열의 끝, 줄끝   |
| \b         | word boundary, 단어의 경계 즉, \w와 \W사이|
| \B         | word boundary가 아닌 경우 |

### modifier(Options)

패턴을 매칭시키는 옵션을 조정한다. 
적용 형태는 다음 중 하나인 경우가 많다:
* (?i)xxxx, (?mi)xxxx
* /xxxx/i, /xxxx/m

| modifier      | 설명                       |
|---------------|----------------------------|
| i             | 대소문자 구분 안함          |
| s(singleline) | .에 new line이 포함됨, ^과 $이 \n을 무시 |
| m(multiline)  | ^과 $을 내부 \n(newline)에 적용 |


## 실습

text
```
Navigate to the home dashboard
The home dashboard is the first dashboard a user sees when they sign in to Grafana. You can also navigate to the home dashboard manually.
---------> click
Hover your cursor over the Dashboards (four squares) icon.
Click Home.
Set the home dashboard for the server
Users with the Grafana Server Admin flag on their account or access to the configuration file can define a JSON file to use as the home dashboard for all users on the server.

[Optional] Convert an existing dashboard into a JSON file
Navigate to the page of the dashboard you want to use as the home dashboard.
Click the Share dashboard icon next to the dashboard title.
In the Export tab, click Save to file. Grafana converts the dashboard to a JSON file and saves it locally.
click
cl
ick this button
```


test: dashboard.*with vs (?s)dashboard.*with

test: (?si)cli.*ck
test: (?si)cli.*?ck
test: (?si)^cli.*ck

test: (?si)cli.*button vs (?si)cli.*?button

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
test: (.+).+\1 ???
test: (.+)([\s-]).+\2\1



```
1000원
2000원
3000원
5000원
10000원
```
test: .+(?=원)  # look ahead


```
1: $600.4
2: $10.25
3: $47.33
4: $112.34
```
test: (?<=$)[0-9.]+  # look behind