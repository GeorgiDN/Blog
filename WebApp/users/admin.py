from django.contrib import admin
from WebApp.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

