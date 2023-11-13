

from django.shortcuts import render, redirect
from user_auth.models.user import User
from user_auth.utiles import send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


def reset_password(request):
    if request.method=='POST':
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            pk=request.session.get('uid')
            user=User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active=True
            user.save()
            #messages.success(request,'Password reset successfully')
            return redirect('user_login')
        else:
            #messages.error(request,'Password doesnt match')
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')