from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="estatelist"),
    path('select_apartment.html', views.select, name="select_apartment"),
    
]