## 제어문 - 1. if

### if 문
[https://wikidocs.net/20](https://wikidocs.net/20)

```
if ... elif ... else
```
* 논리상 빈틈이 없게 구성하는 것이 중요

### 예제1
```
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
```

변형

```
money = True
statement = ''
if money:
    statement = '택시를 타고'
else:
    statement = '걸어서'

statement += ' 가라'  # statement = statement + ' 가라'
print(statement)
```

### 예제2

카드가 있거나 현금이 10000원 이상 있으면 택시를 탄다.

카드가 없거나 현금이 5000원 이상 10000원 미만이면 따릉이를 탄다.

현금만 5000원 미만이면 걷는다.

```
def how_to_get_there(card, money):
    if card or money >= 10000:
        print("택시를 탄다")
    elif ???:
        ???
    elif ???:
        ....
    elif ???: 
    else:
        ....


how_to_get_there(False, 7000)
```

정리:

```
def how_to_get_there(card, money):
    if card:
        print("택시를 탄다")
    else:
        if money >= 10000:
            print("택시를 탄다")
        elif 5000 <= money < 10000:
            print("따릉이를 탄다")
        else:
            print("걷는다.")


how_to_get_there(False, 7000)
``` 

### 예제 3

자동차 주행시간을 도착시간(endtime) - 출발시간(begintime)으로 계산하는데, 자정에 도착한 경우 24대신 0으로 기재한 사람들이 섞여 있다. 이럴 경우 주행 시간을 계산하기 위해 endtime이 0인 경우 24로 보정하는 처리가 필요하다.

```
def get_driving_time(begintime, endtime):
    if endtime == 0:
        endtime = 24
    
    return endtime - begintime


get_driving_time(15, 0)
```

변형

```
def get_driving_time(begintime, endtime):
    endtime = 24 if endtime == 0 else endtime
    return endtime - begintime


get_driving_time(15, 0)
```

