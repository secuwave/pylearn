## 4. Python basic -4

### 딕셔너리 - dict (이어서)
[https://wikidocs.net/16](https://wikidocs.net/16)


### 딕셔너리 샘플

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
    'company': mycompany  # <----- 회사
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

### 딕셔너리 삭제

```
import pprint

pp = pprint.PrettyPrinter(indent=4)

del me['family2']
pp.pprint(me)
```

존재하지 않는 key 자료 삭제

```
search_key = 'gender'
if search_key in me:  # 체크하지 않으면 exception이 발생해 실행이 무단 종료됨
    del me[search_key]
```
cf. exception 처리는 강좌 뒤쪽에서 다룸

### 실습: whois 조회

입력 받은 도메인들에 대한 whois 조회를 해서 정보를 프린트한다.

```
# Whois 조회

import whois  # pip install whois
import pprint

## dir(whois)
## help(whois)

pp = pprint.PrettyPrinter(indent=4)


def read_input():
    input_str = input('체크할 도메인을 입력하세요(,로 분리): ')
    input_list = input_str.split(',')
    return input_list


def check_whois(address_list):
    for addr in address_list:
        winfo = whois.whois(addr)
        pp.pprint(winfo)


if __name__ == '__main__':
    address_list = read_input()
    check_whois(address_list)

```

추가작업
* 데이터가 복잡하니 관심있는 필드만 뽑아서 csv로 보자.
