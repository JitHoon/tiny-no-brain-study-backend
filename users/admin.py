from django.contrib import admin
# 일반적인 admin class 대신 User 전용 admin을 상속받아온다.
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
