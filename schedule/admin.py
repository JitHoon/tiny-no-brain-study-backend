from django.contrib import admin
from .models import Schedule

# Register your models here.


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = ("dplus", "time", "voted", "todo")
    list_filter = ("time", "voted")
    search_fields = ("voted", "todo")
# @ : decoration : 아래 class가 admin.register(Schedule)를 통제한다.
# Schedule model에대한 admin.ModelAdmin class를 상속받음

# 튜플 사용시 ()안에 하나의 element만 들어간다면 ,를 찍어줘야한다.
# ex. search_fields = ("voted",)
