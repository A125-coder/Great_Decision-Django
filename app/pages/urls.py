from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('about_us.html', views.about, name="about"),
    path('guarantee.html', views.guarantee, name="guarantee"),
    path('we_offer.html', views.we_offer, name="we_offer"),
    path('apartments.html', views.apartments, name="apartments"),
]