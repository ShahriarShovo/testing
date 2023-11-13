from django.shortcuts import render, redirect, HttpResponse
from user_auth.models.user import User
from user_auth.utiles import send_verification_email
from django.contrib import messages, auth
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model





def user_register(request):
    
    if request.method == 'POST':
        # print('request  = ', request.POST)
        first_name              =               request.POST.get('first_name')
        last_name               =               request.POST.get('last_name')
        email                   =               request.POST.get('email')
        gender                  =               request.POST.get('gender')
        password                =               request.POST.get('password')
        confirm_password        =               request.POST.get('repeat_password')
        
        

        if email is not None:
            username            =               email.split('@')[0]

            if password         !=              confirm_password:

                return HttpResponse("password Not match")
            
            else:
                user             =               User.objects.create_user(first_name=first_name, 
                                                                            last_name=last_name, 
                                                                            gender_choosed=gender,
                                                                            email=email, username=username, 
                                                                            password=password)
                user.role        =                User.CUSTOMER
                user.sign_up_platform =           User.SITE_SIGNUP
                user.save()

                mail_subject='Active your Account'
                email_template='email/user_ac_active.html'
                send_verification_email(request,user,mail_subject,email_template)
               
                return redirect('thank_you')

        else:
            return HttpResponse("problem Register")

    else:
       
        return render(request, 'accounts/user_register.html')
        
    
    

def activate(request, uidb64,token):
    try:
        uid                        =                  urlsafe_base64_decode(uidb64).decode()
        user                       =                  User._default_manager.get(pk=uid)
    except(User.DoesNotExist, OverflowError, TypeError, ValueError):
        user                       =                  None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active             =                  True
        user.save()
        return redirect('user_login')
        #return HttpResponse('Account verify succesfully')
        #return redirect('user_auth:myaccount')
    else:
        messages.error(request,'Invalid Activetion code')
        return redirect(request,'myaccount')
    



def check_email(request):
    email = request.POST.get('email')

    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse('<div style="color: red"> This email already exists </div>')
    else:
        return HttpResponse('<div style="color: green"> This email is available </div>')