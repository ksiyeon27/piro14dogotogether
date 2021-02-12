# 피로그래밍 14기 프로젝트(5조) : 가치가개


## 팀원소개 / 역할분담

### 1. <a href="https://github.com/jts159753">전태수</a>  (Taesu Jeon, TEAM LEADER)
    1. BackEnd
        - Ajax 통신을 위한 모델 및 뷰 구현(Community 내부)
    2. Frontend
        - Ajax와 Javascript를 이용한 좋아요 기능 구현
        - KAKAOMAP API 적용 담당
    3. IDEA Designer
        - 가치가개 아이디어 제공, 구현에 필요한 기능 구상 발표

### 2. <a href="https://github.com/lisa425">임채원</a> (Chaewon, Im)
    1. Backend
    2. Frontend
        - WireFrame Constructor(Frontend Lead Member) : Adobe XD를 이용한 와이어프레임 개발
        - 와이어프레임 프론트엔드 적용 및 수정(프론트엔드 단 기획, 개발 리딩)
        - 전반 템플릿 구현(Home화면 및 Base.html)

### 3. <a href="https://github.com/yunsik0115">김윤식</a> (Yunsik, Kim)
    1. Backend
        - 커뮤니티 앱 내부 기본 기능(포스트 수정, 생성, 삭제, 목록) 구현
        - Ajax를 이용하여 내부 댓글 기능 사용을 위한 모델, 뷰 함수 구현
    2. Data Mining
        - KAKAO MAP API에 적용하기 위한 데이터 크롤링(반려동물 병원, 위치정보, 기타설명 등등, excel 파일)
        - 데이터 출처 (https://www.culture.go.kr/data/openapi/openapiView.do?id=519&gubun=B)
        - 데이터를 구현된 kakao api에 정보 전달될 수 있도록 수정 작업. (기존 테스트 데이터 -> 실사용데이터)
    3. ReadMe.md 작성

### 4. <a href="https://github.com/ksiyeon27">김시연</a> (Siyeon, Kim)
    1. Backend
        - 소셜 로그인, 로그인, 회원가입을 포함한 accounts 앱 구현당 담당
        - Naver, Google 소셜 로그인 구현
        - 견종별 산책 시간 계산을 위한 데이터 크롤링 담당
    2. Frontend

### 5. <a href="https://github.com/eungi78">조은기</a> (Eungi, Cho)
    1. Backend
        - 소셜 로그인, 로그인, 회원가입을 포함한 accounts 앱 구현 담당
        - Naver, Google 소셜 로그인 구현
        - 견종별 산책 시간 계산을 위한 데이터 크롤링 담당
    2. Frontend
    3. Data Mining
        - 외국 애견 전문 사이트에서 견종 크롤링, 견종 체중 공식과 결과 페이지에 도출할 이미지 크롤링.

## 2. 아이디어 소개
### 1. 아이디어 이름 : 가치가개
>  아이디어 : 개와 같이 가다 -> 강아지의 가치를 존중하자, 반려견들의 산책을 보다 쉽게 할 수 있게 도와주는 서비스

### 2. Main Function
> 1. 사용자 위치 기반으로 반려견 출입 가능 지역 및 산책 가능 지역 개별 제공
> 2. 반려견의 종에 따라 하루 권장 산착거리 및 산책 시간 등 데이터 제공
> 3. 강아지 산책과 관련한 FAQ Section 및 산책 후기 공유
   
### 3. 구현계획
초기 계획은 <a href="markdown/">가치가개 프로그램 발표(발표자 : 전태수)</a> 참고
>   ### 1. Frontend : 임채원님 주도로 Adobe XD를 통해 생성된 <a href="/markdown/img/">와이어프레임</a>을 참고
>   ### 2. BackEnd : Django 내  별 기능 구현 계획
> <table>
> <tr>
> <td>Account</td>
> <td>로그인 및 소셜로그인 기능 구현과 사용자 가입시 동시에 사용자 프로필 생성될 수 있도록 구현 (ODP)</td>
> </tr>
> <tr>
> <td>Blog</td>
> <td>산책 후기 공유를 위한 커뮤니티 구현(글, 댓글, 좋아요 기능 구현 + 권한처리)</td>
> </tr>
> <tr>
> <td>Map</td>
> <td>KAKAOMAP API를 활용하여 사용자 위치 기반 안내 서비스, 사용자 등록 데이터 기반 안내 서비스 구현</td>
> </tr>
> <tr>
> <td>Calculator</td>
> <td>견종별 하루 권장 산책거리 및 시간 제공</td>
> </tr>
> </table>

### 4. 구현에 사용할 라이브러리/플러그인
>#### 1. Django (WebFramework For Python)
> <img src="/markdown/icons/장고 아이콘.png" width="20%"></img>
> <img src="/markdown/icons/piroicon.jpg" width="20%"></img><br/>
> 피로그래밍 14기 세션 및 인강학습기간(12/29/2020 ~ 01/28/2021) 동안 학습한 Django WebFramework를 이용하여<br/>
> 배운 내용을 복습하고, 사이드 프로젝트 구현을 통해 학습한 내용을 한 층 더 굳혀나가는 기회를 얻기 위함입니다.
>#### 2. Pandas (공공API 및 홈페이지 데이터 크롤링)
> 공공 API 데이터를 적절히 크롤링하여, 사용자에게 제공하는데 필요한 데이터를 적절히 정제하여<br/>
> 타 API(카카오) 또는 스스로의 프로그램에 잘 적용하는 방법을 배우기 위해 사용하였습니다.
> #### 3. BeautifulSoup
> 2번 Pandas 사용 이유와 동일합니다.
> #### 4. ChromeWebDriver
> 2번 Pandas 사용 이유와 동일합니다.

## 3. 활동 과정
<img src="/markdown/icons/역할상세.png"></img>
<br/>
> ### 활동 과정 중 고민이었던 부분들!
> - KAKAO API 위치 정보를 얻어오려면 Geolocation이 필요한데 HTTPS 프로토콜을 통해 배포할 수 있을까?
> > HTTPS 배포 세션을 따로 진행하신다고 하신다! // SSL인증 관련 (곧 해결 될 수 있을 것 같다)<br/><br/>
> - 크롤링을 어디서 어떻게 해올것인지(대상 API를 찾아야한다....)
> > 구글링을 통해 공공데이터포털(서울시) 및 해외 사이트에서 대상 정보를 크롤링해오는것으로 해결<br/>
> > &#43; 카카오 맵 API검색기능 활용예정!<br/><br/>
> - 사이트 접속 시도마다 크롤링을 해오면, 비용측면에서 비효율적이지 않을까?
> > Code Review 도중 얻은 Feedback, 크롤링으로 데이터를 만든 이후 저장하여 활용하는 방법으로 변경<br/><br/>
> - Pandas와 Webdriver를 이용해 크롤링으로 엑셀파일까지는 만들었다 -> 어떻게 활용하지?
> > npm convert-xlsx-to-json을 이용하여 엑셀파일 -> json방식으로 변환하여 저장<br/><br/>
> - Json을 통한 데이터 저장 이후 파싱 VS Json 파일을 SQL에 입력 이후 장고에서 사용(어떤게 효율적인가?)
> > <a href="https://softwareengineering.stackexchange.com/questions/235707/using-a-relational-database-vs-json-objects-for-event-activity-data">StackExchange 관련자료</a><br/>
> > <img src="/markdown/etc/조언.jpeg" width="50%"></img> <br/>
> > "변환한 Json파일을 Database에 적용시킬 방법을 알아보도록 하자" -> <a href="https://stackoverflow.com/questions/36123877/django-saving-json-value-to-database-model"> 참고</a><br/><br/>
> - Django Secret Key와 API Secret Key를 어떻게 분리하는게 좋을까?
> >방법 1) 시스템 내부 환경변수에 지정한 뒤, os.environ 이용<br/>
> >방법 2) secrets.json 생성 이후 .gitignore에 추가 -------------------> 현 프로젝트에 사용한 방법<br/><br/>
> - MAP 마커가 많으면 Ajax에서 ERR_INSUFFICIENT_RESOURCES 오류가 나타난다 어떻게 해야할까?
> > 일단 병원. 약국 마커는 기획 의도에 맞지 않다고 판단하여 제거하였으나, <a href="https://apis.map.kakao.com/web/sample/basicClusterer/">Clustering</a>을 통해 해결 가능할듯함.<br/><br/><br/>
> - 팀원간 개발도중 나타나는 pip dependencies로 인한 오류 예방 어떻게 해 할까?
> > 팀원간 가상환경 venv (python -m venv venv)을 이용하고, pip freeze > requirements.txt를 이용해 의존성 기록<br/>
> > 환경 생성할때 pip(3) -r requirements.txt를 이용해 의존성 플러그인 설치 가능
<br/><br/>
> - Create Project 이후에 장고 버전 다운그레이드로 인한 충돌 해결방법?
> > 처음에 팀원간 장고 프로젝트 버전을 합의하고 createproject를 하는게 좋다. (자동으로 최신버전을 깔아버린 탓에..)
> - Class Based View Vs Function Based View?
>> 필요에 따라 사용하기로 함. 처음 배운 내용은 함수형 뷰였기에, 클래스형 뷰는 팀원간 코드 리뷰하는 시간을 가졌음.
