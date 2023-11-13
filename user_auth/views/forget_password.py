from django.shortcuts import render
from user_auth.models.user import User
from user_auth.utiles import send_verification_email
from django.shortcuts import HttpResponse



def forget_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        print("Email------------------", email)

        if User.objects.filter(email=email).exists():
            user=User.objects.get(email__exact=email)

            mail_subject='Reset Your password'
            email_template='email/reset_password.html'

            send_verification_email(request, user,mail_subject,email_template)

            #return redirect('login')
            return HttpResponse("Reset Password link send")
        else:
            pass
            # messages.error(request, " User Not found")
            # return redirect('login')
        
    return render(request, 'accounts/forget_password.html')


