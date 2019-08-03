from django.contrib import admin
##from .models import HelpData
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile2
# Register your models here.
#admin.site.register(HelpData)

"""class ProfileInline2(admin.StackedInline):
    model = Profile2
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline2,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)"""

