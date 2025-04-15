from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'date_joined') 
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('date_joined', )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)