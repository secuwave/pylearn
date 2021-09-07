@echo off

SET count=0
set limit=10

:while
if %count% leq %limit% (
   timeout 1 >nul
   SET /a count=%count% + 1
   echo current count = %count%

   goto :while
)

echo "Do what you want here."