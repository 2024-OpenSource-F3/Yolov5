# 충북대학교 2024 오픈소스 전문프로젝트 Team F3
---
### 프로젝트 소개
충북대학교 2024년도 오픈소스 전문프로젝트 신재혁 교수님반의 Team F3의 고기관련 정보 알림앱 "꼬기꼬기"입니다.
꼬기꼬기는 1인가구와 같이 고기를 소비하는데 있어서 정보가 부족한 사람들에게 고기의 등급이나 정보를 제공해주는 앱입니다.

### 프로젝트 팀 구성원
| 이름 | 학번 | 분야 |
|---|---|---|
| 서범수 | 2019019014 | 인공지능 |
| 이형진 | 2020039018 | 백엔드 |
| 원명진 | 2021041011 | 프론트엔드 |

### Requirement

```pip install -r requirements.txt```
python 3.0 버전 필요
pytorch 1.8 이상의 버전 필요

### How to use
실행을 하기전 위의 requirements.txt 요소들을 받습니다.
이후 모델을 사용하기위해 app.py 를 실행시켜 서버를 local로 오픈합니다.

```Python app.py```

이후 http: IP address :4740 포트로 formData 형식에서 file 이라는 이름으로 file 형식의 이미지를 첨부하여 보냅니다.
그럼 response로 json 형식의 타입에 맞추어 class, X-max , X-min , Y-max , Y-min , name , confidence가 응답으로 오게됩니다.
이때 name은 탐지된 객체의 이름 , confidence는 정확도입니다.
confidence가 높을수록 객체를 정확하게 탐지한것입니다.
