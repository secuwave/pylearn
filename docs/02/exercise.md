# Whois 조회

```python
import whois

def whois_check(address):
    result = whois.whois(address)
    return str(result)


order = "www.naver.com,www.google.com,www.openbase.co.kr,www.daum.net,www.seoul.go.kr,www.seoul.go.kr,www.seoul.go.kr"
todo_list = order.split(',')

for address in todo_list:
    ret = whois_check(address)
    print(ret)


```
