# 정규표현 & python에서 정규표현 사용 기초

## 정규표현
[OpenbaseSecurity_LearningScript_04.pdf](./OpenbaseSecurity_LearningScript_04.pdf)


## python에서 정규표현 사용 기초

search() vs match() vs findall()

1. re.match() - 문자열의 처음위치부터 정규식과 일치 여부를 검사한다. 
   따라서 일치하는 부분이 문자열 중간에 나오면 매칭되지 않음으로 판단한다.
2. re.search() - 문자열의 모든 영역에서 정규식과 일치 여부를 검사한다.
3. re.findall() - match(), search()는 일치 여부 확인에 중점을 두므로 
   일단 매치되는 1건을 확인하고 끝난다. findall()은 모든 일치하는 부분을 검색한다.


### 실습
#### 1. 숫자 검색

```python
import re

dummy_string = '12.aaabbcccdream333-taa(20181203-001)'

print('---------------------')
print('문자열 "{}"에서 정규식 "\\d+" 일치를 테스트\n'.format(dummy_string))
m = re.match(r'\d+', dummy_string)  # \d+ : 숫자. 1, 11, 234555 ...
print('match m = {}'.format(m))

m = re.search(r'\d+', dummy_string)
print('search m = {}'.format(m))

m = re.findall(r'\d+', dummy_string)
print('findall m = {}'.format(m))
```

출력:
```
---------------------
문자열 "12.aaabbcccdream333-taa(20181203-001)"에서 정규식 "\d+" 일치를 테스트

match m = <_sre.SRE_Match object; span=(0, 2), match='12'>
search m = <_sre.SRE_Match object; span=(0, 2), match='12'>
findall m = ['12', '333', '20181203', '001']
```

#### 2. 문자 검색

```python
import re

dummy_string = '12.aaabbcccdream333-taa(20181203-001)'

print('---------------------')
regex = r'a+'  # a+ : a로만 이뤄진 길이 1개 이상의 문자열: a, aa, aaa, aaaa ....
print('문자열 "{}"에서 정규식 "{}" 일치를 테스트\n'.format(dummy_string, regex))

m = re.match(regex, dummy_string)
print('match m = {}'.format(m))

m = re.search(regex, dummy_string)
print('search m = {}'.format(m))

m = re.findall(regex, dummy_string)
print('findall m = {}'.format(m))

for i in m:
    print('matched item: {}'.format(i))
```

출력:
```
---------------------
문자열 "12.aaabbcccdream333-taa(20181203-001)"에서 정규식 "a+" 일치를 테스트

match m = None
search m = <_sre.SRE_Match object; span=(3, 6), match='aaa'>
findall m = ['aaa', 'a', 'aa']
matched item: aaa
matched item: a
matched item: aa
```