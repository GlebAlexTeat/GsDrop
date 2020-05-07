from django.contrib import admin
from .models import Users, Gun, Case



@admin.register(Users)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Money', 'Admin')

@admin.register(Gun)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title_gun', 'grade', 'quality','img_road_gun','value','startrec')

@admin.register(Case)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'img_road',)