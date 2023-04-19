from django.contrib import admin
from .models import Schedule

# Register your models here.


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
# @ : decoration : 아래 class가 admin.register(Schedule)를 통제한다.
# Schedule model에대한 admin.ModelAdmin class를 상속받음
