# 예외처리


## 설명 내용

[https://wikidocs.net/30](https://wikidocs.net/30)

[python document - Built-in exceptions](https://docs.python.org/ko/3/library/exceptions.html)



## 예외처리 실습

#### 파일 읽기

```python
with open('data/test.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line)
```


#### 파일이 없는 경우

파일이 없는 경우 예외 발생의 예시

```python
with open('data/none', 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line, end='')
```
파일이 없기 때문에 발생하는 exception ==> _FileNotFoundError_

```python
Traceback (most recent call last):
  File "E:/WorksTemp/dummy/15/exc.py", line 31, in <module>
    file_read2()
  File "E:/WorksTemp/dummy/15/exc.py", line 23, in file_read2
    with open("data/none", 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/none'

```

#### 파일이 없어서 생기는 예외의 처리

```python
with open('data/none', 'r') as f:
    try:
        while True:
            line = f.readline()
            if not line: break
            print(line, end='')
    except FileNotFoundError as e:
        print(f'File error: {e}, creating the file...')
        open('data/none', 'w').close()
```

```python
try:
    with open('data/none', 'r') as f:
        while True:
            line = f.readline()
            if not line: break
            print(line, end='')
except FileNotFoundError as e:
    print(f'File error: {e}, creating the file...')
    open('data/none', 'w').close()
```

#### 복수의 예외에 대한 처리

1 - 여러가지 예외가 발생하는 경우의 처리 - 개별 처리

10000을 입력받은 숫자로 나누고, 결과를 'data2/result.txt에 기록한다.

```python
def ex_test(file):
    test_number = 10000
    user_input = input('dividend: ')
    dividend = int(user_input)
    result = test_number/dividend

    with open(file, 'w', encoding='utf-8') as f:
        f.write(result)

    print('result=', result)


if __name__ == '__main__':
    file = 'data2/result.txt'
    ex_test(file)

```

위 코드에서 발생 가능한 exception은?
* FileNotFoundError - 파일이나 디렉토리가 없음 
* ValueError - 연산이나 함수가 올바른 형이지만 부적절한 값을 가진 인자를 받음. int()함수에 int변환이 불가능한 알파벳인자.
* ZeroDivisionError - 나누는 수가 0
* TypeError - 연산이나 함수가 부적절한 형의 객체에 적용될 때 발생. 함수 인자로 문자열을 받아야 하는데, 숫자를 받음.

2 - FileNotFoundError 예외처리
```python
def ex_test(file):
    test_number = 10000
    user_input = input('dividend: ')
    dividend = int(user_input)

    result = test_number/dividend
    try:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(result))
    except FileNotFoundError as e:
        print(f'error: {e}')

    print('result=', result)


if __name__ == '__main__':
    file = 'data2/result.txt'
    ex_test(file)

```

3 - ValueError 예외처리
```python
def ex_test(file):
    test_number = 10000
    user_input = input('dividend: ')

    try:
        dividend = int(user_input)
    except ValueError as e:
        print(f'error: {e}')
        print('dividend number set to default 100')
        dividend = 100

    result = test_number/dividend

    try:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(result))
    except FileNotFoundError as e:
        print(f'error: {e}')

    print('result=', result)


if __name__ == '__main__':
    file = 'data2/result.txt'
    ex_test(file)

```

4 - ZeroDivisionError 예외처리
```python
def ex_test(file):
    test_number = 10000
    user_input = input('dividend: ')

    try:
        dividend = int(user_input)
    except ValueError as e:
        print(f'error: {e}')
        print('Dividend number set to default 100')
        dividend = 100

    try:
        result = test_number/dividend
    except ZeroDivisionError as e:
        print(f'error: {e}')
        print('Result set to zero')
        result = 0

    try:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(result))
    except FileNotFoundError as e:
        print(f'error: {e}')

    print('result=', result)


if __name__ == '__main__':
    file = 'data2/result.txt'
    ex_test(file)

```

5 - 3가지 예외를 하나로 묶어서 처리하기
* 
```python
def ex_test(file):
    test_number = 10000
    try:
        user_input = input('dividend: ')
        dividend = int(user_input)
        result = test_number / dividend

        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(result))
    except ValueError as e:
        print(f'error: {e}')
    except FileNotFoundError as e:
        print(f'error: {e}')
    except ZeroDivisionError as e:
        print(f'error: {e}')
        result = 0

    print('result=', result)


if __name__ == '__main__':
    file = 'data2/result.txt'
    ex_test(file)

```

6 - 3가지 예외를 하나로 묶어서 처리하기 - 2
```python
def ex_test(file):
    test_number = 10000
    try:
        user_input = input('dividend: ')
        dividend = int(user_input)
        result = test_number / dividend

        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(result))
    except Exception as e:
        print(f'error: {e}')
        result = 0

    print('result=', result)


if __name__ == '__main__':
    file = 'data2/result.txt'
    ex_test(file)

```
## TCP 포트 스캔 예제

지정한 호스트에 포트가 열려 있는지 스캔한다.

### 소켓 생성 정보

1 - 소켓 생성 함수 형식

```python
sock = socket.socket (socket_family, socket_type)
```
2 - Socket Family
* AF_INET: IPv4
* AF_INET6: IPv6

3 - Socket Type:
* SOCK_STREAM: TCP
* SOCK_DGRAM: UDP

### IPv4 TCP 소켓 생성
```python
import socket

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
```

### 호스트 이름을 IPv4 주소형식으로 변환
```python
remote_host_ip = socket.gethostbyname("hostname")
```
### 지정한 호스트에 대해 특정 범위 포트 스캔

```python
import socket
import sys
from datetime import datetime

# 스캔할 호스트 입력받기
remote_host = input("스캔할 호스트 네임(IP): ")

# 예외처리를 위해 try... except 적용
try:
    remote_host_ip = socket.gethostbyname(remote_host)
except socket.gaierror as e:
    print(f'호스트주소 에러: {e}')
    sys.exit()

# "스캔중...." 메시지 프린트
print("-" * 60)
print("스캔중.... Host address: ", remote_host_ip)
print("-" * 60)

# 스캔 시작시간 저장. 스캔 소요시간 계산에 이용
t1 = datetime.now()

# 스캔할 포트(범위)를 지정한다.
# port_range = [21, 22, 23, 25, 53, 80, 111, 135, 137, 139, 443, 445, 512, 623, 3000, 3389, 5432, 8080]
port_range = range(1,2014) # 1~1024
# port_range = range(1,101) # 1~100
try:
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((remote_host_ip, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        else:
            print("Port {}: 	 Close".format(port))
        sock.close()
except KeyboardInterrupt as e:
    print(f'Ctrl+C 입력됨')
    sys.exit()
except socket.error as e:
    print(f'기타 소켓 에러: {e}')
    sys.exit()

# 종료시간
t2 = datetime.now()

# 스캔 소요시간 계산
elapsed_time = t2 - t1

# 스캔 소요시간 프린트
print("스캔 소요시간: ", elapsed_time)
```