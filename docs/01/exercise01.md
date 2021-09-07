# html 자바스크립트 생일축하

## 생일축하 인사
```html
<!doctype html>
<html>
<head>
    <title>Test</title>
</head>
<body>
    <h1>greeting</h1>
</body>
<script>
    birthday_member = "오픈베이스"
    member = prompt("이름을 입력하세요: ");
    if (member == birthday_member) {
        alert(member + "님 생일축하합니다!");
    }
    else {
        alert(member + "님 반갑습니다!");
    }
</script>
</html>

```
## 자바스크립트 js(greeting.js) 파일로 분리 작성
### html 파일
```html
<!doctype html>
<html>
<head>
    <title>Test</title>
</head>
<body>
    <h1>greeting</h1>
</body>
<script src="greeting.js"></script>
<!-- 
<script>
    birthday_member = "오픈베이스"
    member = prompt("이름을 입력하세요: ");
    if (member == birthday_member) {
        alert(member + "님 생일축하합니다!");
    }
    else {
        alert(member + "님 반갑습니다!");
    }
</script>
-- >
</html>
```

### 분리한 greeting.js

```js
birthday_member = "오픈베이스"
member = prompt("이름을 입력하세요: ");
if (member == birthday_member) {
    alert(member + "님 생일축하합니다!");
}
else {
    alert(member + "님 반갑습니다!");
}
```