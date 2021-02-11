from django.db import models
from django.conf import settings
"""
Don't Use the User Model Directly
https://stackoverflow.com/questions/34305805/django-foreignkeyuser-in-models
"""

class areaselection(models.Model):
    TYPE = "kr"
    REGION_CATEGORY_CHOICES = ((TYPE, '전체'), (TYPE, '강남구'), (TYPE, '강동구'), (TYPE, '강북구'), (TYPE, '강서구'), (TYPE, '관악구'), (TYPE, '광진구'), (TYPE, '구로구'), (TYPE, '금천구'),
                               (TYPE, '노원구'), (TYPE, '도봉구'), (TYPE, '동대문구'), (TYPE, '동작구'), (TYPE, '마포구'), (TYPE, '서대문구'), (TYPE, '서초구'),
                        (TYPE, '성동구'), (TYPE, '성북구'), (TYPE, '송파구'), (TYPE, '양천구'), (TYPE, '영등포구'), (TYPE, '용산구'), (TYPE, '은평구'), (TYPE, '종로구'),
                        (TYPE, '중구'), (TYPE, '중랑구'))
    map_region = models.CharField(choices=REGION_CATEGORY_CHOICES, max_length=5, blank=True)

class placeAddByUser(models.Model):
    """
    사용자에 의해 추가될 장소를 저장하기 위한 모델
    name = 지역 이름
    xmap, ymap = 지도 api를 위한 좌표 저장
    created_by => 등록자 표기를 위한 모델 -> 등록자 탈퇴시 탈퇴한 유저로 설정되도록 디폴트 설정
    """
    TYPE = "kr"
    CATEGORY_CHOICES = ((TYPE, "식당"), (TYPE, "카페"), (TYPE, "공원"))
    name = models.CharField(max_length=30)
    region = models.CharField(max_length=30, blank=True)
    xmap = models.DecimalField(max_digits=9, decimal_places=6)
    ymap = models.DecimalField(max_digits=9, decimal_places=6)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, null=True, blank=True) #카테고리 추가
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default="탈퇴한 유저")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

class currentLocation(models.Model):
    """
    유저의 현재 좌표를 표시하기 위한 모델
    x좌표 - decimalfield
    y좌표 - decimalfield https://www.python2.net/questions-188688.htm referenced
    """
    xmap = models.DecimalField(max_digits=9, decimal_places=6)
    ymap = models.DecimalField(max_digits=9, decimal_places=6)


class userLocationInfo(models.Model):
    """
    feedback 반영 : userlocationInfo따로 분리하여 관리
    user의 경우 1:1 필드 이용하여 사용자 정보 필드 별도로 저장
    https://wikidocs.net/6651
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    userLocation = models.ForeignKey(currentLocation, on_delete=models.CASCADE,)