from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def about(request):
    data = {"header_h1": "Про <span>Нас</span>",
            "header_p": "Головна >> Про нас"}
    return render(request, 'pages/about_us.html', context=data)


def guarantee(request):
    data = {"header_h1": "НАШІ <span>ГАРАНТІЇ</span>",
            "header_p": "Головна >> Гарантії"}
    return render(request, 'pages/guarantee.html', context=data)

def we_offer(request):
    data = {"header_h1": "ЩО <span>ПРОПОНУЄМО</span>",
            "header_p": "Головна >> Що пропонуємо"}
    return render(request, 'pages/we_offer.html', context=data)

def apartments(request):
    data = {"header_h1": "НЕРУХОМІСТЬ",
            "header_p": "Головна >> Квартири"}
    return render(request, 'pages/apartments.html', context=data)