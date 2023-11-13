from django.contrib import admin
from django.urls import path, include
from .views.user_registration import user_register, activate, check_email
from .views.user_login import user_login, myaccount
from .views.thank_you import thank_you
from .views.forget_password import forget_password
from .views.user_dashboard import user_dashboard
from .views.user_logout import user_logout
from .views.google_login import google_login
from .views.google_login import google_callback
from .views.git_hub_login import github_callback, github_login
from .views.facebook_login import facebook_login,facebook_callback #facebook_login_callback
from .views.reset_password import reset_password
from .views.reset_password_validate import reset_password_validate
from .views.settings import settings

#app_name='user_auth'

urlpatterns = [
   
    path('login/', user_login, name='user_login'),
    path('user_registration/', user_register, name='user_registration'),
    
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('thank_you/', thank_you, name='thank_you'),
    path('check_email', check_email, name='check_email'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('logout/', user_logout, name='user_logout'),
    path('myaccount/', myaccount, name='myaccount'),
    path('settings/', settings, name='settings'),
    path('update_user_info', settings, name='update_user_info'),


    #google auth
    path('auth/google_login/', google_login, name='google_login'),
    path('auth/google_callback/', google_callback, name='google_callback'),

    #git hub
    path('auth/github/', github_login, name='github_login'),
    path('auth/github_callback/', github_callback, name='github_callback'),

    #facebook 

    path('facebook-login/', facebook_login, name='facebook_login'),
    path('facebook-callback/', facebook_callback, name='facebook_callback'),
    # Reset password
    path('forget_password/', forget_password, name='forget_password'),
    path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    #path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    path('reset_password/', reset_password, name='reset_password'),


    
    

    


]
