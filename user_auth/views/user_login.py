from django.shortcuts import render, redirect, HttpResponse
from user_auth.models.user import User
from django.contrib.auth.decorators import login_required
from user_auth.utiles import detectUser
from django.contrib.auth import login, authenticate
from django.db.models import Q

#from user_auth.EmailBackend import EmailPhoneUsernameAuthenticationBackend

# def user_login(request):
    
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         print("Email--------------", email)
#         print("Password------------", password)

#         user=authenticate(email=email, password=password)
#         #user=authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             return redirect('user_login')
#     return render(request,'accounts/user_login.html')

   
def user_login(request):
    
    detect = request.POST.get('username')
    passowrd = request.POST.get('password')

    print("User name --------------------------",detect)
    print("Password --------------------------",passowrd)
        
    match = User.objects.filter(
            Q(username = detect)|
            Q(email = detect)
           
        ).first()
    
    if match:
        email = match.email
        print("Email-----------------------", email)
        user = authenticate(request,email=email, password=passowrd)
        print("User-----------------------", user)

        if user is not None:
            login(request,user)

            return redirect('index')
        else:
            return HttpResponse("its not working")
    else:
        
        return render(request,'accounts/user_login.html')
    
    
#@login_required(login_url='login')
def myaccount(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)