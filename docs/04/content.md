## 4. Python basic -3

### 딕셔너리 - dict
[https://wikidocs.net/16](https://wikidocs.net/16)

#### iterable(collections.Iterable)

* iterable 객체 - 반복 가능한 객체
* 대표적 iterable 타입 - list, tuple(튜플), dict, set(집합), str(문자열), bytes, range
* dict(딕셔너리)는 iterable의 속성을 가짐

### 딕셔너리

* key-value pair로 구성되어 key를 이용해 조작
* 리스트, 튜플처럼 iteration도 가능하지만 순서가 의미있지는 않음

### 딕셔너리 샘플

```
me = {
    'name': 'ykkim',
    'age': 30,
    'address': 'seoul',
    'phone': '010-999-8888',
    'birth': '10/02',
    'job': 'engineer',
    'family': [
        {'role': 'father', 'name': 'kimsj', 'age': 74},
        {'role': 'mother', 'name': 'kimkh', 'age': 69},
        {'role': 'sister', 'name': 'kimjh', 'age': 35},
        {'role': 'brother', 'name': 'kimdh', 'age': 30}
    ],
    'family2': {  # family를 다른 형태로 정의, 역할을 key로 하는 dict
        'father': {'name': 'kimsj', 'age': 74},
        'mother': {'name': 'kimkh', 'age': 69},
        'sister': {'name': 'kimjh', 'age': 35},
        'brother': {'name': 'kimdh', 'age': 30}
    },
    'house': [  # 집은 여러채 일 수 있으므로 list
      'seoul', 'suwon', 'pusan', 'daejeon'
    ],
    'weight': None
}

mycompany = {
    'name': 'openbase',
    'birth': '1992/09/16',
    'employee': ['kim', 'park', 'lee'],
    'location': 'seoul'
}
```
#### 값 구하기

* key를 []에 지정하거나 get() method에 지정해서 값을 구할 수 있는데 get()을 권장
* get()을 쓰면 key가 없는 경우 에러대신 None을 리턴

```
print(me.get('name'))
print(me['name'])

print(me.get('family'))
print(me['family'])

print(me.get('family')[0])
print(me['family'][0])
```

#### 아빠 나이 구하기1 - family(라스트)에서

```
for member in me.get('family'):
    if member.get('role') == 'father':
        print('father\'s age: {}'.format(member.get('age')))
```

#### 아빠 나이 구하기2 - family2(딕셔너리)에서

```
print('father\'s age: {}'.format(me.get('family2').get('father').get('age')))
```

#### 내 정보에 회사 추가하기

* 회사 딕셔너리를 mycompany라는 변수에 정의하고
* mycompany를 me안에 company라는 키의 값으로 넣는다.

```
mycompany = {
    'name': 'openbase',
    'birth': '1992/09/16',
    'employee': ['kim', 'park', 'lee'],
    'location': 'seoul'
}

me = {
    'name': 'ykkim',
    'age': 30,
    'address': 'seoul',
    'phone': '010-999-8888',
    'birth': '10/02',
    'job': 'engineer',
    'company': mycompany,  # <----- 회사
    'family': [
        {'role': 'father', 'name': 'kimsj', 'age': 74},
        {'role': 'mother', 'name': 'kimkh', 'age': 69},
        {'role': 'sister', 'name': 'kimjh', 'age': 35},
        {'role': 'brother', 'name': 'kimdh', 'age': 30}
    ],
    'family2': {  # family를 다른 형태로 정의, 역할을 key로 하는 dict
        'father': {'name': 'kimsj', 'age': 74},
        'mother': {'name': 'kimkh', 'age': 69},
        'sister': {'name': 'kimjh', 'age': 35},
        'brother': {'name': 'kimdh', 'age': 30}
    },
    'house': [  # 집은 여러채 일 수 있으므로 list
      'seoul', 'suwon', 'pusan', 'daejeon'
    ],
    'weight': None
}
```
#### 회사 정보 업데이트 하기

me.update({key: value})

```
me.update({'company': mycompany})  # me에 key가 있으면 value교체

me.update({'company2': mycompany})  # me에 key가 없으면 key & value 추가
```
#### 딕셔너리 iteration - item

```
for item in me.items():  # item은 (key, value) 형태의 튜플
    print(item)
```

#### 딕셔너리 iteration - item tuple unpack

```
for key, value in me.items():
    print(f'key = {key}, value = {value}')
```
#### 딕셔너리 iteration - using key

* 딕셔너리 key들

```
keys = me.keys()  # keys의 타입은 dict_keys, 리스트와 같은 방식으로 iteration 가능
print(keys)

key_list = list(keys)
```

* key를 이용해서 딕셔너리 iteration

```
for key in me.keys():
    print(f'key={key}, value={me.get(key)}')
```

#### 특정 key가 있을 경우에 그 값을 추출(프린트)하려면

```
### 1
if 'company' in me.keys():
    print(me.get('company'))

### 2
if 'company' in me:
    print(me.get('company'))
```

* (권장)사용하는 값이 반복되면 상수(constant value)로 정의

```
search_key = 'company'
if search_key in me:
    print(me.get(search_key))
```

#### key가 없으면? - [] 조회의 문제

```
search_key = 'annual_income'  # annual_income 키는 존재하지 않음
print(me.get(search_key))  # None 리턴
print(me[search_key])  # <--- key error 발생으로 실행 종료
```

#### key가 없으면 기본값 부여

get으로 key를 조회하면 key가 없어 값이 None일 경우, 기본값(대체값) 부여를 할 수 있음

```
search_key = 'annual_income'
my_annual_income = me.get(search_key, 3000000)  # 연간소득 자료가 없을 경우 300만원으로 기본값 지정
print(my_annual_income)
```

* 기본값 설정 주의!! key가 있는데 그 값이 None이면 기본값(대체값)이 부여되지 않음
```
search_key = 'weight'
my_weight = me.get(search_key, 70)  # weight 키가 있고 값이 None이므로 70이 적용되지 않음
print(my_weight)
```

### 실습: XML <-> dictionary <-> json

* 딕셔너리를 중심으로 XML -> 딕셔너리 -> json 변환

참고: [XML example(Microsoft)](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms762271(v=vs.85))

(1) XML을 딕셔너리로 변환하기

```
import xmltodict
import pprint


xml_string = """<?xml version="1.0"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications 
      with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, 
      an evil sorceress, and her own childhood to become queen 
      of the world.</description>
   </book>
   <book id="bk103">
      <author>Corets, Eva</author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology 
      society in England, the young survivors lay the 
      foundation for a new society.</description>
   </book>
</catalog>
"""


# print(xml_string)

pp = pprint.PrettyPrinter(indent=4)
catalog_dict = xmltodict.parse(xml_string, dict_constructor=dict)  # catalog: dict type
pp.pprint(catalog_dict)
```

(2) 딕셔너리를 json으로 변환하기

```
import json

json_string = json.dumps(catalog_dict, indent=4)
print(json_string)
```

(3) json을 dict로 변환하기

```
catalog_dict_new = json.loads(json_string)
pp.pprint(catalog_dict_new)
```