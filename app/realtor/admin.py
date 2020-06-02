from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email", "city", "hire_date")
    list_display_links = ("id", "name", "phone","email")
    list_per_page = 15
    search_fields = ("name", "phone")
    list_filter = ('name', 'hire_date', 'mvr', 'city')


admin.site.register(Realtor, RealtorAdmin)
