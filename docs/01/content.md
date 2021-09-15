# 1. Quick Start

[pylearn_01.pdf](./pylearn_01.pdf)

---------------------
## Python 환경
### Python

인터프리터의 배포 버전은 여러가지가 있을 수 있는데 일반 작업은 기본 python으로 가능하며, 모듈 추가 필요시 pip로 설치하면 된다. 번거로운 모듈 추가를 줄이기 위해서 Anaconda와 같이 다양한 모듈이 포함된 배포판을 설치할 수도 있다. 선택의 문제이며, 어느 쪽이 절대적으로 좋은 것은 아니다. 
Anaconda는 사용이 편리하지만 설치 파일이 크고 디스크 사용량이 많다.

#### python.org
* [https://www.python.org](https://www.python.org)
* 인터프리터 다운로드 및 문서 참고

#### Anaconda
* Anaconda download: 
  * [https://www.anaconda.com/download](https://www.anaconda.com/download) 또는 
  * [https://www.anaconda.com/products/individual-d](https://www.anaconda.com/products/individual-d)
* Python 인터프리터의 배포판 중 하나. 다양한 데이터 처리 모듈이 동반 패키징 됨.


### Python 버전 선택

대부분 인터프리터들과 달리 Python은 버전 2.x ~ 3.x 사이에 하위 호환성이 없다. 버전2 코드를 버전3에서 실행하려면 수정해야한다. 

버전3에서 개선,추가된 것들이 많으므로 다음 경우가 아니면 버전3을 사용한다.

#### 부득이 버전 2를 써야하는 경우
1. 스크립트를 돌리는 환경이 Python 버전2인데 업그레이드 할 수 없다.
2. 이미 쓰고 있는 스크립트를 수정하려고 하는데, 그 스크립트가 Python 버전2 이다. -> 버전3으로 수정할 수 있는 분량이라고 하더라도 수정후 기존 동작을 검증할 자신이 없으면 수정하지 않는 게 좋다. #사실상 하지 말 것.

---------------------

## 에디터

* 메모장, vi 
* notepad++ 
* VS Code(Visual Studio Code)
* jupyter notebook (ipython): python cli처럼 interactive하게 python 코드를 실행할 수 있어 데이터 분석이나 python 연습에 많이 쓰임
* PyCharm이나 다른 Python 전용 에디터
  * [pycharm](https://www.jetbrains.com/ko-kr/pycharm/download/)
  
---------------------


* [Python 환경 및 테스트 실행](./python_setup.md)

### 실습:
* 1에서 100까지 더하기
* python 코드 파일 구조