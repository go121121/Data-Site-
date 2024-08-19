from django.contrib import admin
from .models import data_application 
# Register your models here.


class MemberAdmin(admin.ModelAdmin): 
    list_display=('first_name','last_name','phone','Date')
admin.site.register(data_application,MemberAdmin)