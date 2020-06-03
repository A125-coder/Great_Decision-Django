from django.shortcuts import render
from .models import Apartments

# Create your views here.
def index(request):
    apartments = Apartments.objects.order_by("-list_date").filter(is_published = True)

    context = {
        'apartments':apartments
    }
    return render(request, "pages/apartment.html", context)

def select(request):
    data = {"header_h1": "КВАРТИРИ <span>ДЛЯ ВАС</span>",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='apartment.html'>Квартири для вас</a> >> Двокімнатна квартира"}
    return render(request, 'pages/select_apartment.html', context=data)