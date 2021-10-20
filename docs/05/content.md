## 4. Python basic -5

### 집합 - set
[https://wikidocs.net/1015](https://wikidocs.net/1015)

#### iterable(collections.Iterable)

* iterable 객체 - 반복 가능한 객체
* 대표적 iterable 타입 - list, tuple(튜플), dict, set(집합), str(문자열), bytes, range
* dict(딕셔너리)는 iterable의 속성을 가짐

### 집합

* 수학에서의 집합과 유사한 집합적 객체
* 중복 불가
* 순서 없음(Unordered)
  * 리스트와 튜플은 ordered

### 집합 생성

set1 = {6, 5, 4, 3, 2, 1}
set2 = set([6, 5, 4, 3, 2, 1])

```
my_set = set([5, 4, 3, 2, 1, 2, 3, 4])
print(my_set)
```

```
my_set2 = ("HELLO")
print(my_set2)
```

### 집합 속성

순서 안중요: 

```
member_set = {'kim', 'lee', 'park', 'choi', 'nam'}
print(member_set)  # Unordered
```

리스트 같은 인덱싱(인덱스로 개별 요소 접근 등 인덱스 기반의 액세스)이 안 된다. 인덱스 액세스를 하려면 리스트로 변환해야 한다.

```
member_list = list(member_set)
print(type(member_list))

print(member_list[-1])  # 맨 끝 멤버 구하기

```

### 교집합, 합집합, 차집합

```
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)

# 합집합
print(s1 | s2)

# 차집합
print(s1 - s2)
print(s2 - s1)
```

### 변형

add

```
s1 = set([1, 2, 3])
s1.add(4)
print(s1)
```

update

```
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)
```

remove

```
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
```

### whois 조회 - 업그레이드

* 입력받은 도메인 리스트에 space가 들어가 있으면?
* 입력받은 도메인 리스트에 중복된 도메인이 있으면?

```
# Whois 조회

import whois  # pip install whois
import pprint

## dir(whois)
## help(whois)

pp = pprint.PrettyPrinter(indent=4)


def read_input():
    input_str = input('체크할 도메인을 입력하세요(,로 분리): ')
    # TODO
    input_list = temp.split(',')
    return input_list


def check_whois(address_list):
    # TODO
    for addr in ???:
        winfo = whois.whois(addr)
        pp.pprint(winfo)


if __name__ == '__main__':
    address_list = read_input()
    check_whois(address_list)

```