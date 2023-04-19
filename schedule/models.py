from django.db import models

# Create your models here.


class Schedule(models.Model):

    """Model Definition for Schedule"""

    dplus = models.PositiveIntegerField()  # 스터디 차수
    place = models.TextField()  # 스터디 장소
    time = models.DateTimeField(auto_now=True)  # 스터디 시간
    voted = models.PositiveIntegerField()  # 스터디 투표 인원
    todo = models.TextField()  # 스터디 내용
