# 디렉토리의 파일 목록을 CSV/엑셀 파일로 내보내기

## 순서

1. 지정한 경로의 하위에 있는 모든 파일 목록을 수집한다.

2. 파일 목록을 CSV로 내보낸다.
  * 파일의 이름에 특정 패턴이 있는 경우만 선택
  
3. 파일 목록을 엑셀로 내보낸다.
  * 파일의 이름에 특정 패턴이 있는 경우 빨간색으로 표시
  * 확장자 정보 추가


### 실습

#### 모듈

```python
import os
import re
import openpyxl  # as excel  # pip install openpyxl
import openpyxl.styles as excel_style
```

#### 20xx 연도 숫자가 들어간 워드,파워포인트,엑셀 파일을 찾는 정규표현 정의&컴파일

```python
RE_FILE = re.compile(r'.*20\d{2}.*\.(pptx?|docx?|xlsx?)$')  # 숫자 20xx가 포함된 ppt(x), doc(x), xls(x) 파일
```

#### 디렉토리의 모든 파일 목록 수집 함수

```python

def get_file_list(check_path):
    files = []
    for (path, dir, file) in os.walk(check_path):
        # print(path, '--', dir, '---', file)
        for filename in file:
            files.append((path, filename, os.path.join(path, filename)))
    return files
```


#### CSV로 내보내기 함수

```python
def export_csv(check_path, output_file):
    file_info = get_file_list(check_path)
    print(f'file found: {len(file_info)}')

    with open(output_file, 'w', encoding='utf-8') as f:
        for path, filename, fullpath in file_info:
            f.write(f'{path},{filename},{fullpath}\n')
```

* 개선1: 특정 패턴(앞서 정의한 20xx연도가 포함된 워드/엑셀/파워포인트) 파일만 추출
* 개선2: CSV에 컬럼 헤더 추가

```python
def export_csv(check_path, output_file):
    file_info = get_file_list(check_path)
    print(f'file found: {len(file_info)}')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'경로,파일이름,전체경로\n')   # <---- 개선1
        for path, filename, fullpath in file_info:
            m = re.search(RE_FILE, filename)  # <---- 개선2
            if m:
                f.write(f'{path},{filename},{fullpath}\n')

```
#### 엑셀로 내보내기 함수

```python
def export_excel(check_path, output_file):
    file_info = get_file_list(check_path)
    print(f'file found: {len(file_info)}')

    wbook = openpyxl.Workbook()
    wsheet = None
    try:
        wsheet = wbook.create_sheet('my_test')
        wbook.remove(wbook['Sheet'])  # <---- default 워크시트 'Sheet' 제거
    except Exception as e:
        print(f'work sheet error: {e}')
        exit(1)

    wsheet.append(['디렉토리', '파일이름', '전체경로', '확장자'])

    for path, filename, fullpath in file_info:
        stem, ext = os.path.splitext(filename)
        wsheet.append([path, filename, fullpath, ext])

    wbook.save(output_file)
    wbook.close()
```

* 개선: 셀 컨트롤
  * bold, 글자색, 셀 배경색 적용
  * 경로의 모든 파일을 엑셀에 기록하되, 정규표현 패턴에 일치(20xx년 파워포인트,워드,엑셀)하는 파일인 경우 빨간색 굵은 글씨로 표현

```python
def export_excel_adv(check_path, output_file):
    file_info = get_file_list(check_path)
    print(f'file found: {len(file_info)}')

    font_default = excel_style.Font(size=10, color='000000')
    font_default_bold = excel_style.Font(size=10, color='000000', bold=True)
    font_white = excel_style.Font(size=10, color='FFFFFF')
    font_red_bold = excel_style.Font(size=10, color='CC0000', bold=True)
    fill = excel_style.PatternFill(start_color='132A40', fill_type='solid')

    wbook = openpyxl.Workbook()
    wsheet = None
    try:
        wsheet = wbook.create_sheet('my_test')
        wbook.remove(wbook['Sheet'])
    except Exception as e:
        print(f'work sheet error: {e}')
        exit(1)

    row = 1  # 엑셀의 row는 1부터 시작
    cell = wsheet.cell(row=row, column=1, value='디렉토리')
    cell.font = font_white
    cell.fill = fill

    cell = wsheet.cell(row=row, column=2, value='파일이름')
    cell.font = font_white
    cell.fill = fill

    cell = wsheet.cell(row=row, column=3, value='전체경로')
    cell.font = font_white
    cell.fill = fill

    cell = wsheet.cell(row=row, column=4, value='확장자')
    cell.font = font_white
    cell.fill = fill

    for path, filename, fullpath in file_info:
        row += 1
        font = font_default

        cell1 = wsheet.cell(row=row, column=1, value=path)
        cell1.font = font_default
        
        cell2 = wsheet.cell(row=row, column=2, value=filename)
        cell2.font = font_default
        
        cell3 = wsheet.cell(row=row, column=3, value=fullpath)
        cell3.font = font_default

        stem, ext = os.path.splitext(filename)
        cell4 = wsheet.cell(row=row, column=4, value=ext)
        cell4.font = font_default

        m = RE_FILE.search(filename)
        if m:
            cell2.font = font_red_bold  # 패턴에 일치하면 빨강 bold

    wbook.save(output_file)
    wbook.close()
```