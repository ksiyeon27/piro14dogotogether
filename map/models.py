from django.db import models

# Create your models here.
<<<<<<< Updated upstream

class Spot(models.Model):
	name = models.CharField()
	lat = models.Decimal()
	lng = models.Decimal()
	possible
	infor.....

# 유저 위치 기반으로 뭘 하려고 한다?

class User(models.Model):
	이름, 아이디, 비번, 소셜 정보, ...
	userLocation = models.ForeignKey(UserLocation)

# 자주 업데이트.
class UserLocation(models.Model):
	lat = models.Decimal()
	lng = models.Decimal()



# crawling
저장 포맷 : TXT vs JSON
txt, csv, xsl

f = open('a.txt', 'w')
f.write('')
f.close()


f = open('a.txt', 'r')
content = f.read()
return content

{"a" : 1, "b": 2}


데이터 저장
1. DB
- 정보가 바뀌고, 관련해서 활용많이 할 때
- ex) 유저 현 위치 받아서 10키로 이내 핫스팟 알려주기
- ex) 유저 반려견끼리 연결시켜주기 1키로 이내
- 읽고 쓰는 속도가 빠름. 비용(CPU 연산량)이 비싸

2. 파일
- 느린데, 쓸 수 있음.

3. 클라우드
=======
>>>>>>> Stashed changes
