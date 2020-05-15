from django.contrib import admin
from .models import Profile, Gun, Case
#_____________________________________________________________________
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



# @admin.register(Profile)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('user', 'Money')

@admin.register(Gun)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title_gun', 'grade', 'quality','img_road_gun','value','startrec')

@admin.register(Case)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'img_road',)


#_____________________________________________________________________
class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'

# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline, )



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'Money', 'Rang']


admin.site.register(Profile, ProfileAdmin)