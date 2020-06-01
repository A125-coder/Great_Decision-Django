from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def about(request):
    data = {"header_h1": "Про <span>Нас</span>",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='about_us.html'>Про нас</a>"}
    return render(request, 'pages/about_us.html', context=data)


def guarantee(request):
    data = {"header_h1": "НАШІ <span>ГАРАНТІЇ</span>",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='guarantee.html'>Гарантії</a>"}
    return render(request, 'pages/guarantee.html', context=data)

def we_offer(request):
    data = {"header_h1": "ЩО <span>ПРОПОНУЄМО</span>",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='we_offer.html'>Що пропонуємо</a>"}
    return render(request, 'pages/we_offer.html', context=data)

def apartments(request):
    data = {"header_h1": "КВАРТИРИ <span>ДЛЯ ВАС</span>",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='apartment.html'>Квартири для вас</a>"}
    return render(request, 'pages/apartment.html', context=data)

def order(request):
    data = {"header_h1": "ЗАМОВИТИ",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='order.html'>Замовити</a>"}
    return render(request, 'pages/order.html', context=data)

def testimonials(request):
    data = {"header_h1": "ВІДГУКИ",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='testimonials.html'>Відгуки</a>"}
    return render(request, 'pages/testimonials.html', context=data)

def discounts(request):
    data = {"header_h1": "ЗНИЖКИ",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='discounts.html'>Знижки</a>"}
    return render(request, 'pages/discounts.html', context=data)

def contact_us(request):
    data = {"header_h1": "КОНТАКТИ",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='contact_uss.html'>Контакти</a>"}
    return render(request, 'pages/contact_us.html', context=data)

def prices(request):
    data = {"header_h1": "НАШІ <span>ЦІНИ</span>",
            "header_p": "<a href='index.html'>Головна</a> >> <a href='prices.html'>Наші ціни</a>"}
    return render(request, 'pages/prices.html', context=data)