from django.contrib import admin
from .models import CustomUser,Products

admin.site.register(CustomUser)

admin.site.register(Products)