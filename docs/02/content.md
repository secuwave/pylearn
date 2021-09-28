## 2. Python basic

### [Python 善 - import this](./201.md)

### 자료형 - 숫자

[https://wikidocs.net/12](https://wikidocs.net/12)

* 정수(int) : 정수
* 실수(float) : 소수점이 포함된 숫자, e 표기법도 가능. 다른 언어에서 실수를 float과 double로 나누는데, Python은 float 타입만 있음
* 8진수(int) : 정수, 0o로 시작하는 8진법 표현
* 16진수(int) : 정수, 0x로 시작하는 16진법 표현

```
a = 3
type(a)
```
```
b = 3.1
type(b)
```

e표기법
```
c = 15e-2
d = 1.5E+4
e = 0.5E3
```

16진수
```
f = 0x11
```

나눗셈
```
g = 7/4
h = 7.0/4
i = 7/4.0
j = 7//4
```


mod
```
k = 27%6
```
* 왜 유용할까?

### 자료형 - 문자열

[https://wikidocs.net/13](https://wikidocs.net/13)

* wrapping: " or ' ??
* escape

```
print('\n')
print('\a')
```

* 문자열 iteration

```
dummy = 'this is a test.'

for i in dummy:
    print(i)
```

* split and join

```
dummy = 'this is a test.'
dummy_list = dummy.split(' ')
dummy_back = ' '.join(dummy_list)
```

### iterable(collections.Iterable)

* iterable 객체 - 반복 가능한 객체
* 대표적 iterable 타입 - list, dict, set, str, bytes, tuple, range


### import 와 __main__


### 실습:

* 100번째 마다 진도 표시하기

* 100개의 빵을 7명에게 임의로/균등하게 분배하기

* import this 만들기

