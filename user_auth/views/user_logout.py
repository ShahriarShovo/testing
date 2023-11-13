from django.shortcuts import redirect
from django.contrib import messages, auth

def user_logout(request):
    auth.logout(request)
    return redirect('index')