## 4. Python basic -3

### 딕셔너리 - dict
[https://wikidocs.net/16](https://wikidocs.net/16)

#### iterable(collections.Iterable)

* iterable 객체 - 반복 가능한 객체
* 대표적 iterable 타입 - list, tuple(튜플), dict, set(집합), str(문자열), bytes, range
* list는 iterable의 속성을 가짐

### 딕셔너리

* key-value pair로 구성되어 key를 이용해 조작
* 리스트, 튜플처럼 iteration도 가능하지만 순서가 의미있지는 않음


### 딕셔너리 예제

```
me = {
    'name': 'ykkim',
    'age': 30,
    'address': 'seoul sonpa',
    'phone': '010-999-8888',
    'birth': '10/02',
    'job': 'engineer',
    'family': [
        {'role': 'father', 'name': 'kimsj', 'age': 74},
        {'role': 'mother', 'name': 'kimkh', 'age': 69},
        {'role': 'sister', 'name': 'kimjh', 'age': 35},
        {'role': 'brother', 'name': 'kimdh', 'age': 30}
    ],
    'family2': {  # family를 다른 형태로 정의
        'father': {'name': 'kimsj', 'age': 74},
        'mother': {'name': 'kimkh', 'age': 69},
        'sister': {'name': 'kimjh', 'age': 35},
        'brother': {'name': 'kimdh', 'age': 30}
    }
    'house': [
      'seoul', 'suwon', 'pusan', 'daejeon'
    ]
}

mycompany = {
    'name': 'openbase',
    'birth': '1992/09/16',
    'member': ['kim', 'park', 'lee'],
    'location': 'Seoul'
}
```
#### 값 구하기

```
print(me.get('name'))
print(me['name'])

print(me.get('family')[0])
print(me['family'][0])

print(me.get('family'))
print(me['family'])
```

#### 아빠 나이 구하기1 - family1에서

```
???
```

#### 아빠 나이 구하기2 - family2에서

```
???
```

#### 내 정보에 회사 추가하기

```
???
```

#### 딕셔너리 iteration - item

```
???
```

#### 딕셔너리 iteration - unpack

```
???
```

#### 딕셔너리 iteration - using key

* 딕셔너리 key들

```
???
```

* key iteration

```
???
```

#### 특정 key가 있을 경우에 그 값을 프린트

```
if 'company' in me.keys():
    print(me.get('company'))

```

* 사용하는 값이 반복되면 상수로 정의한다.

```
?
if ? in me.keys():
    print(me.get(?))

```

#### 특정 key가 없으면? - [] 조회의 문제

```
search_key = 'annual_income'
print(me.get(search_key))
print(me[search_key])  # error
```

#### 특정 key가 없으면 기본값 부여

get으로 key를 조회하면 key의 값이 없을 경우, 기본값(대체값) 부여를 할 수 있다.

```
search_key = 'annual_income'
my_annual_income = me.get(search_key, 3000000)
print(my_annual_income)
```
