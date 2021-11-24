## 파일 읽고 쓰기

[https://wikidocs.net/26](https://wikidocs.net/26)


### 파일 열기

* (새로)쓰기
```
f = open('new1.txt', 'w')
f.close()
```

* 추가쓰기
```
f = open('new1.txt', 'a')
f.close()
```

* 읽기
```
f = open('new1.txt', 'r')
f.close()
```

### 파일에 쓰기

* (새로)쓰기
```
for i in range(5):
    f = open('new1.txt', 'w')
    text = input('입력: ')
    f.write(text)
    f.close()
```

* 추가쓰기
```
for i in range(5):
    f = open('new1.txt', 'a')
    text = input('입력: ')
    f.write(text)
    f.close()
```

### 파일 읽기

* [테스트 로그](./0612portal.log.txt)

* 한 줄 읽어보기
```
filename = '0612portal.log'
f = open(filename, 'r')
line = f.readline()
print(line)
f.close()
```

* 모든 줄 읽어보기
```
filename = '0612portal.log'
f = open(filename, 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()
```

#### 파일 읽고 쓰기

```
ifile = '0612portal.log'
ofile = 'output.txt'

iif = open(ifile, 'r')
of = open(ofile, 'w')

while True:
    line = iif.readline()
    if not line:
        break
    of.write(line)

iif.close()
of.close()

```
> diff 0612portal.log output.txt


#### 내용 골라서 쓰기

```
ifile = '0612portal.log'
ofile = 'output.txt'

iif = open(ifile, 'r')
of = open(ofile, 'w')

while True:
    line = iif.readline()
    if not line:
        break
    if 'start' in line.lower():
        of.write(line)
    elif 'stop' in line.lower():
        of.write(line)
    elif 'fail' in line.lower():
        of.write(line)
iif.close()
of.close()

```

### 파일 close와 context manager(with)

* 파일을 썼으면 반드시 CLOSE!!

```
file = open('a.txt', 'w')
try:
    file.write('TEST')
finally:
    file.close()
```

* context manager with를 이용한 똑같은 코드
  * with 영역이 끝나면 자동으로 열린 자원을 close한다.

```
with open('a.txt', 'w') as of:
    of.write('TEST')
```

#### 내용 골라서 쓰기 - with context 방식으로 개선

```
ifile = '0612portal.log'
ofile = 'output.txt'

with open(ifile, 'r') as iif:
    with open(ofile, 'w') as of:
        while True:
            line = iif.readline()
            if not line:
                break
            if 'start' in line.lower():
                of.write(line)
            elif 'stop' in line.lower():
                of.write(line)
            elif 'fail' in line.lower():
                of.write(line)

```
