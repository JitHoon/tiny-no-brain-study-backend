from django.db import models
# django에서 제공해주는 user class를 상속받아 pw기능 등 보편적인 기능들을 불러와 활용
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass
