# 피로그래밍 14기 프로젝트(5조) : 가치가개


## 1. 팀원소개 / 역할분

### 1. 전태수  (Taesu Jeon, TEAM LEADER)
    1. BackEnd
        - Ajax 통신을 위한 모델 및 뷰 구현(Community 내부)
    2. Frontend
        - Ajax와 Javascript를 이용한 좋아요 기능 구현
        - KAKAOMAP API 적용 담당
    3. IDEA Designer
        - 가치가개 아이디어 제공, 구현에 필요한 기능 구상 발표

### 2. 임채원 (Chaewon, Im)
    1. Backend
    2. Frontend
        - WireFrame Constructor(Frontend Lead Member) : Adobe XD를 이용한 와이어프레임 개발
        - 와이어프레임 프론트엔드 적용 및 수정(프론트엔드 단 기획, 개발 리딩)
        - 자세한 와이어프레임은 다음 링크를 참조 (<a href="/markdown/img/">와이어프레임</a>)

### 3. 김윤식 (Yunsik, Kim)
    1. Backend
        - 커뮤니티 앱 내부 기본 기능(포스트 수정, 생성, 삭제, 목록) 구현
        - Ajax를 이용하여 내부 댓글 기능 사용을 위한 모델, 뷰 함수 구현
    2. Data Mining
        - KAKAO MAP API에 적용하기 위한 데이터 크롤링(반려동물 병원, 위치정보, 기타설명 등등, excel 파일)
        - 데이터 출처 (https://www.culture.go.kr/data/openapi/openapiView.do?id=519&gubun=B)
        - 크롤링을 통해 구현된 kakao api에 정보 전달될 수 있도록 수정 작업. (기존 테스트 데이터 -> 실사용데이터)

### 4. 김시연 (Siyeon, Kim)
    1. Backend
        - 소셜 로그인, 로그인, 회원가입을 포함한 accounts 앱 구현당 담당
        - Naver, Google 소셜 로그인 구현
        - 견종별 산책 시간 계산을 위한 데이터 크롤링 담당

### 5. 조은기 (Eungi, Cho)
    1. Backend
        - 소셜 로그인, 로그인, 회원가입을 포함한 accounts 앱 구현 담당
        - Naver, Google 소셜 로그인 구현
        - 견종별 산책 시간 계산을 위한 데이터 크롤링 담당

##2. 아이디어 소개
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
