from django.contrib import admin

# Register your models here.
from.models import Complain, Users,UserPic

admin.site.register(Users)
admin.site.register(Complain)
admin.site.register(UserPic)