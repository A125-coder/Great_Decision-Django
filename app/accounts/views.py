from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    return render(request, "accounts/login.html")


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

    return render(request, "accounts/register.html")


def logout(request):
    return render(request, "accounts/logout.html")


def dashboard(request):
    return render(request, "accounts/dashboard.html")
