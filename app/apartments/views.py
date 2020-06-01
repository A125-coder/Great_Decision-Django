from django.shortcuts import render
from .models import Apartments

# Create your views here.
def index(request):
    apartments = Apartments.objects.order_by("-list_date").filter(is_published = True)

    context = {
        'apartments':apartments
    }
    return render(request, "pages/apartment.html", context)