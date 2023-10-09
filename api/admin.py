from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import make_password


# Register your models here.
#
# class MyUserCreationForm(UserCreationForm):
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.password = make_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class MyUserChangeForm(UserChangeForm):
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.password = make_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
#
#
# class MyUserAdmin(UserAdmin):
#     add_form = MyUserCreationForm
#     form = MyUserChangeForm
#

admin.site.register(User)
