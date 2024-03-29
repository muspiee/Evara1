from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Customusers, address
import random


# Create your views here.

def user_auth(request):
    return render(request, 'AUTH/login_reg.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_verified == True:
                login(request, user)
                messages.error(request, "login success.")
                return redirect('home')
            else:
                messages.error(request, "Please verify the account")
        else:
            messages.error(request, 'No User Found.')
    return redirect('user_auth')



def reg_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        otp1 = request.POST.get('otp')
        if password == password1:
            if Customusers.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken. Please choose another.')
            elif Customusers.objects.filter(email=email).exists():
                messages.error(request, 'Email is taken. Please choose another.')
            else:
                otp = random.randint(0000, 9999)
                user = Customusers.objects.create_user(username=username, email=email, password=password,profile_pic=img, otp=otp)
                user.set_password(password)
                username = f'{username}'
                subject = 'Account Verification OTP'
                message = f'Hi {username}, Thanks for registering to Evara, here is you OTP:{otp}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, 'Check your email for OTP')
                return redirect('user_auth')


        else:
            messages.error(request, 'Password not matched. Please try again.')
            return redirect('user_auth')

    return redirect('user_auth')


def otp_verify(request):
    if request.method =="POST":
        otp = request.POST.get('otp')
        if otp:
            user = Customusers.objects.filter(otp=otp).first()
            if user:
                user.is_verified = True
                user.save()
                messages.error(request, "Account verified, Please login.")
            else:
                messages.error(request , 'No User Found.')
    return redirect('user_auth')

def user_logout(request):
    logout(request)
    messages.error(request, "User logged out!") 
    return redirect('user_auth')


def reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            user = Customusers.objects.get(email = email)
            print(user)
            if user:
                otp = random.randint(0000, 9999)
                user.otp = otp
                user.save()
                subject = 'Account Verification OTP'
                message = f'Hi {user.username}, Thanks for registering to Evara, here is you OTP:{otp}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
            else:
                otp = random.randint(0000, 9999)
                user.otp = otp
                user.save()
                subject = 'Account Verification OTP'
                message = f'Hi {user.username}, Thanks for registering to Evara, here is you OTP:{otp}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)

    return render(request, 'AUTH/reset.html')


def otp_reset(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        new_pass = request.POST.get('new_pass')
        if otp:
            user.Customusers.objects.filter(otp=otp).first()
            if user:
                user.password = new_pass
                user.set_password(new_pass)
                user.save()
                messages.error(request, 'Password Reset Done, Please Login')



def dashboard(request):
    user = request.user
    user_details = Customusers.objects.get(username=user)
    add = address.objects.filter(user=user)

      
    return render(request, 'dash/dash.html', {'add':add, 'user_details':user_details})



        



 