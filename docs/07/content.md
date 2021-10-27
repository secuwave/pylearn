## 6. Python basic -7

### 변수 variable
[https://wikidocs.net/18](https://wikidocs.net/18)


__jump to python 내용이 좋으므로 별도 요약 하지 않음__


### 변수 값과 변경

```
a = 3
b = a

print(a)
print(b)
```

```
b = b+1

print(a)
print(b)

```

### 변수 값과 변경 - 리스트
```
a = [1,2,3]
b = a

print(a)
print(b)
```

```
b[1] = 100
print(a)
print(b)
```
a와 b는 같은 리스트를 가리킴

새 변수에 값만 같게 복사하려면?

``` 
from copy import copy
a = [1, 2, 3]
b = copy(a)

```
또는 
```
a = [1, 2, 3]
b = a.copy()
```

### 변수 간 값의 교환 (swap)

a와 b의 값을 바꾸고 싶을 때.
* python이 아닌 언어
```
a = 3
b = 10

# swap
temp = a
a = b
b = temp

print(a, b)
```

* python: swap을 위해 임시 저장소가 필요 없음
```
a = 3
b = 10

a, b = b, a

print(a, b)
```
