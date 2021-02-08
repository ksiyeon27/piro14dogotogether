from django.db import models

from django.db import models
from django.conf import settings
"""
Don't Use the User Model Directly
https://stackoverflow.com/questions/34305805/django-foreignkeyuser-in-models
"""
class placeAddByUser(models.Model):
    """
    사용자에 의해 추가될 장소를 저장하기 위한 모델
    name = 지역 이름
    xmap, ymap = 지도 api를 위한 좌표 저장
    created_by => 등록자 표기를 위한 모델 -> 등록자 탈퇴시 탈퇴한 유저로 설정되도록 디폴트 설정
    """
    name = models.CharField(max_length=30)
    xmap = models.DecimalField(max_digits=9, decimal_places=6)
    ymap = models.DecimalField(max_digits=9, decimal_places=6)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default="탈퇴한 유")
    created_at = models.DateTimeField(auto_now_add=True)

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

