## 5. Python basic -6

### Boolean
[https://wikidocs.net/17](https://wikidocs.net/17)


* True - 참
* False - 거짓

### bool 값을 변수에 직접 정의

```
a = True
b = False
```

### 비교, 논리 연산의 결과값은 bool
```
1 == 1
2 == 3
```
```
2 != 3
```
```
2 < 3
```
```
a = 2 < 3
```

아래 코드의 결과는?
``` 
if "python":
    print('T')
else:
    print('F')
```

* 값이 없거나 비어 있으면 거짓
* 논리 연산의 결과 틀렸으면 거짓

체크함수

```
def check_true_false(value):
    if value:
        print(f'{value} is TRUE!!')
    else:
        print(f'{value} is FALSE!!')
```
체크
```
check_true_false('')
```
```
check_true_false([])
```
```
check_true_false(0)
```
```
check_true_false(-1)
```

### bool 타입으로 cast

```
bool('test')
```
```
bool([])
```
```
bool(0)
```

### 리스트에 들어 있는 모든 숫자들에 대해 100을 곱하고 처리한 값은 제거

무한 실행 loop:

```
while True:
    print(f'inside while loop')
```

```
count = 0
while 1:
    count = count + 1
    print(f'inside while loop: {count}')
```

loop 순환 실행이 너무 빠르다!!! 

```
import time

count = 0
while 1:
    count = count + 1
    print(f'inside while loop: {count}')
    time.sleep(1)
```

리스트의 모든 멤버를 꺼내서 100을 곱하기

```
a = [1, 2, 3, 4]
```

while loop 반복
```
while True:
    print(a.pop()*100)
    if len(a) == 0:
        break
```
개선
```
while len(a):
    print(a.pop()*100)
```

더 개선
```
while a:
    print(a.pop()*100)
```
