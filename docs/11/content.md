## 사용자 입력과 출력

[https://wikidocs.net/25](https://wikidocs.net/25)


### input: 사용자의 표준 입력을 받는다.
* 문자열로 받는다!

```
number = input("숫자를 입력하세요: ")
숫자를 입력하세요:
```

#### 입력값에 곱하기 처리하기
```
def multiply10(n):
    return n*10

number = input("숫자를 입력하세요: ")
숫자를 입력하세요:

ret = multiply10(number)
print(ret)

```
* 수정이 필요한 부분은?


### 숫자를 맞출때까지 계속 시도하는 게임

```
secret = 55

intro = '''
.. 내가 생각하는 숫자를 맞춰보세요
.. 그만하고 싶으면 '포기'를 입력하세요
'''

prompt = '''숫자: '''

def is_matched(guess):
    if guess == secret:
        return True


print(intro)

while True:
    print(prompt, end='')
    guess = input()

    if guess == '포기':
        print('.... 포기하셨습니다. Bye!', end='')
        break
    else:
        if is_matched(int(guess)):
            print('.... 정답입니다!', end='')
            break
print('--> 맞추기 종료')
```
