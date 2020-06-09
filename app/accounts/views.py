from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    # if request.method == 'GET':
    #     user_name = request.GET.username
    #     password = request.GET.password

    #     if User.objects.filter(username!=user_name).exists():
    #         print("User doesn't exist. Please register")
    #         return redirect('register')

    #         if User.objects.filter(password!=password).exists():
    #             return redirect('register')
            
    #         else:
    #             return redirect('index')
    #     else:
    #         return redirect('index')

    data = {"header_h1": "Увійти в кабінет",
            "header_p": "<a href='index.html'>Головна</a> >> Увійти в кабінет"}

    return render(request, "accounts/login.html",context=data)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['Name']
        last_name = request.POST['Surname']
        user_name = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                print("User exists")
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    print("Email exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=user_name,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    print("You are registered. Please Login.")
                    return redirect('login')
        else:
            print("Password don't match")
            return redirect('register')

    data = {"header_h1": "Реєстрація",
            "header_p": "<a href='index.html'>Головна</a> >> Реєстрація"}

    return render(request, "accounts/register.html", context=data)


def logout(request):
    return render(request, "accounts/logout.html")


def dashboard(request):
    return render(request, "accounts/dashboard.html")
