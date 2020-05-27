from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email","birth_date")
    list_display_links = ("id", "name", "phone","email")
    list_per_page = 15


admin.site.register(Realtor, RealtorAdmin)
