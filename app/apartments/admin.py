from django.contrib import admin
from .models import Apartments

# Register your models here.


class ApartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'price', 'is_published','is_favorite')
    list_display_links = ('id', 'title', 'price')
    list_editable = ('is_published', 'is_favorite', )
    search_fields = ("address", "city", "title", "price", "realtor")
    list_filter = ("city", "realtor", "square_all", "list_date", 'is_favorite')
    list_per_page = 30


admin.site.register(Apartments, ApartmentsAdmin)
