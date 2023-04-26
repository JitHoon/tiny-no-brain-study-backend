from django.db import models
# django에서 제공해주는 user class를 상속받아 pw기능 등 보편적인 기능들을 불러와 활용
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # editable=False 를 통해 사용하지 않음을 명시
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    # 우리의 새로운 데이터를 추가
    name = models.CharField(max_length=150)


# users/models.py

# 아래 주석은 실제 AbstractUser 파일에 있는 기능들이다. 아래 기능들을 사용하지 않도록 overroad 것이다.
'''
first_name = models.CharField(_("first name"), max_length=150, blank=True)
last_name = models.CharField(_("last name"), max_length=150, blank=True)
'''
