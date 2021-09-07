# Windows Batch - 특정 파일 찾아서 복사하기

```bat
@echo off
set RootDir=C:\data\source
set DstDir=C:\data\destination
mkdir %DstDir%
rem root 하위 디렉토리를 순환하면서 모든 png 파일을 특정 위치로 복사
rem /r: recursive folders, %%f : each file 
for /r "%RootDir%" %%f in (*.png) do copy "%%f" "%DstDir%"
echo copy finished
```
