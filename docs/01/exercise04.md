# 리눅스 - 시스템 상태 체크

## 시간, 포트상태, 메모리 상태 체크

```bash
#! /bin/bash

date
netstat -an | grep 5601
vmstat
echo -------------------
```

### 실행

```bash
$ chmod 755 my_script.sh
$ ./my_script.sh
```

## 3초마다 연속 모니터링

```bash
#! /bin/bash

while [ 1 ]
do
    date
    netstat -an | grep 5601
    vmstat
    echo -------------------
    sleep 3
done
```

## 파일에 저장

```bash
#! /bin/bash

while [ 1 ]
do
    date >> report.dat
    netstat -an | grep 5601 >> report.dat
    vmstat >> report.dat
    echo ------------------- >> report.dat
    sleep 3
done
```

### 프로세스 확인

```bash
$ ps –ef | grep bash
```

### 데이터 모니터링

```bash
$ tail –f ./report.dat
```



