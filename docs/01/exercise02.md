# html 자바스크립트 Base64로 변환하기

## Base64 변환하기


```html
<!doctype html>
<html>
  <head>
    <title>Test2</title>
  </head>
  <body>
    <form id="testform">
      Input: <input type="text" name="user_input">
      <input type="button" value="Base64 변환" onclick="convert2Base64()"></input>
      ->
      <input type="text" name="base64">
    </form>
  </body>
  <script type="text/javascript">
    function convert2Base64()
    {
      result = window.btoa(document.forms["testform"]["user_input"].value)
      document.forms["testform"]["base64"].value = result;
    }
  </script>
</html>
```

## 실행 결과

![result](https://secuwave.github.io/secure3/learn_script/01/exercise021.png)
