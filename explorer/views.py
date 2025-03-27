from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'explorer/home.html')


def cesium_data_view(request):
    return render(request, 'explorer/cesium_data.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            send_welcome_email(user.email)  # Send welcome email after successful signup
            return redirect('cesium_data')  # Change this to 'home' instead of 'cesium_data'
    else:
        form = UserCreationForm()
    return render(request, 'explorer/signup.html', {'form': form})
        

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cesium_data')  # Change this to 'home' instead of 'cesium_data'
    else:
        form = AuthenticationForm()
    return render(request, 'explorer/login.html', {'form': form})


def send_welcome_email(user_email):
    subject = 'Welcome to My Website'
    message = 'Thank you for signing up!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
