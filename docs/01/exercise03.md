# Linux Shell – 명령 프롬프트

## 프롬프트에서 덧셈하기

```bash
$ a=1
$ b=100

$ ret1=$a+$b
$ echo $ret1
???

$ ret2=`expr $a + $b`
$ echo $ret2
???

$ let ret3=$a+$b
$ echo $ret3
???

```

## 결과

```bash
$ a=1
$ b=100

$ ret1=$a+$b
$ echo $ret1
1+100

$ ret2=`expr $a + $b`
$ echo $ret2
101

$ let ret3=$a+$b
$ echo $ret3
101

```