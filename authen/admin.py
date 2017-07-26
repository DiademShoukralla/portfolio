from django.contrib import admin

from authen.forms import MyUserChangeForm, RegisterForm
from .models import User
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = RegisterForm
    fieldsets = UserAdmin.fieldsets[:-1] + (
            (None, {'fields': ()}),
    )


admin.site.register(User, MyUserAdmin)
