# 열화상 감시 시스템

![Home](https://user-images.githubusercontent.com/64760329/210748985-53e1c9f8-a0b6-496a-9994-ca9bc3003580.PNG)
![Thermal Home Page](https://user-images.githubusercontent.com/64760329/210751995-0a24aac3-e416-4d56-86f5-4d8c39f31a34.gif)

![DB Data](https://user-images.githubusercontent.com/64760329/210748913-b42a9637-4243-4b60-a8c5-4acf2983a894.PNG)
![Thermal DB](https://user-images.githubusercontent.com/64760329/210751587-9998bdb3-58a7-4d4c-883f-0dd5ece0c540.gif)






### 참조사이트

- https://picamera.readthedocs.io/en/release-1.13/recipes1.html
- raspberry pi camera 해설 : https://potatoggg.tistory.com/192
- video motion detection capture python : https://s-engineer.tistory.com/107
- video motion detection C++ : https://hyongdoc.tistory.com/410
- video motion detection python

- ***

- pip install opencv-python
- pip install opencv-contrib-python
- python -m motion_detected.py -v VMD_test.mp4

***

### test_i2c.py 구동방법

- Linux 운영체제
- python 3버전
- opencv 설치 : pip install opencv-python
- opencv contrib 설치 : pip install opencv-contrib-python
- Lepton.py 설치 : 비트 버킷 src 디렉토리 내부 Lepton.py

***

### Django 구동방법

- python 환경 구성
- 가상환경 실행 mysite 폴더내에 site/Scripts/activate
- ~/mysite/python manage.py runserver 구동한다.
- 브라우저에서 http://127.0.0.1:8000
***

### 이메일 발송 예제 구동방법

- ~/send/views.py 에서 상세설정 가능 (주석참고)
- ~/sendemail/python manage.py runserver 구동한다.

***
