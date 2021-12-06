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


### character class

| 정규표현식  | 설명                                     | 등가의 다른 정규표현식     |
|------------|------------------------------------------|---------------------------|
| .          | 모든 문자, 개행문자(new line)을 제외하고.  | [^\n]                     |
| [...]      |||
| [^...]     |||
| \w         |||
| \W         |||
| \s         |||
| \S         |||
| \d         |||
| \D         |||

[[:class:]]: alnum, alpha, ascii, blank, cntrl, digit, graph, lower, print, punct, space, upper, xdigit

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

### grouping

| 정규표현식  | 설명                                     | 등가의 다른 정규표현식     |
|------------|------------------------------------------|---------------------------|
| .          | 모든 문자, 개행문자(new line)을 제외하고.  | [^\n]                     |

### modifier

## 실습



# list

* greedy
* grouping
* assertion
* modifier
