## 제어문 - 2. while

### while 문
[https://wikidocs.net/21](https://wikidocs.net/21)


```
while condition:
    body
```
* 특정 조건부 반복 실행 또는 무한 반복 실행
* 조건부 반복일 경우는 종료/break 조건이 명확한지 확인
* 무한 반복시 실행주기(간격)에 신경써야함


### 예제

명령어를 입력 받는다. 명령어가 'quit'이 아니면 계속 반복한다.
```
prompt = '''
.. init: 시작값 설정
.. p   : plus 1
.. m   : minus 1
.. quit

Enter command: '''

command = ''
while command != 'quit':
    print(prompt, end='')
    command = input()
    print(f'  >> your command: {command}')
```

명령어를 입력 받아 'init'이면 number 초기값을 설정한다.

```
number = 0

prompt = '''
.. init: 시작값 설정
.. p   : plus 1
.. m   : minus 1
.. quit

Enter command: '''


command = ''
while command != 'quit':
    print(prompt, end='')
    command = input()

    if command == 'init':
        print('.... number value: ', end='')
        number = int(input())

    print(f'  >> your command: {command}, current number: {number}')
```

명령어를 입력 받아 'plus'이면 number를 1 증가, 'minus'면 1감소시킨다.
```
number = 0

prompt = '''
.. init: 시작값 설정
.. p   : plus 1
.. m   : minus 1
.. quit

Enter command: '''


def plus(n):
    return n + 1


def minus(n):
    return n - 1


command = ''
while command != 'quit':
    print(prompt, end='')
    command = input()

    if command == 'init':
        print('.... number value: ', end='')
        number = int(input())
    elif command == 'p':
        number = plus(number)
    elif command == 'm':
        number = minus(number)

    print(f'  >> your command: {command}, current number: {number}')
```

명령어를 입력 받아, 지원하지 않는 명령어이면 다시 하라고 알려준다.
```
number = 0

prompt = '''
.. init: 시작값 설정
.. p   : plus 1
.. m   : minus 1
.. quit

Enter command: '''


def plus(n):
    return n + 1


def minus(n):
    return n - 1


command = ''
while command != 'quit':
    print(prompt, end='')
    command = input()

    if command == 'init':
        print('.... number value: ', end='')
        number = int(input())
    elif command == 'p':
        number = plus(number)
    elif command == 'm':
        number = minus(number)
    else:
        print(f'  !!!! ERROR: invalid command [{command}]')
        continue
    print(f'  >> your command: {command}, current number: {number}')
```

끝? quit을 입력해도 invalid command로 처리되므로 수정
```
number = 0

prompt = '''
.. init: 시작값 설정
.. p   : plus 1
.. m   : minus 1
.. quit

Enter command: '''


def plus(n):
    return n + 1


def minus(n):
    return n - 1


command = ''
while True:
    print(prompt, end='')
    command = input()

    if command == 'init':
        print('.... number value: ', end='')
        number = int(input())
    elif command == 'p':
        number = plus(number)
    elif command == 'm':
        number = minus(number)
    elif command == 'quit':
        print(f'your input: {command}, GOOD BYE!!')
        break
    else:
        print(f'  !!!! ERROR: invalid command [{command}]')
        continue
    print(f'  >> your command: {command}, current number: {number}')
print('---> exit this program')
```