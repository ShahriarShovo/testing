from django.shortcuts import render, HttpResponse, redirect
from user_auth.models.google_data import Google_Data
from user_auth.models.user import User
from user_auth.models.user_profile import Profile
from django.shortcuts import get_object_or_404
from orders.models.billing_address import BillingAddress



def settings(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    print("user--------", user_profile)
    user_first_name= user.first_name
    user_last_name=user.last_name
    user_phone = user.phone
    user_email = user.email
    if request.method == "POST":
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                print("first_name--------------",first_name)
                print("last_name--------------",last_name)
                print("phone--------------",phone)
                print("email--------------",email)
                user.first_name = first_name
                user.last_name = last_name
                user.phone = phone
                user.email = email
                user.save()
                return redirect('settings')
    elif request.method == "POST":
            user_billing_address = BillingAddress.objects.get(user=user)
            
            
            

    context={
            'user_first_name' :user_first_name,
            'user_last_name' : user_last_name,
            'user_phone' : user_phone,
            'user_email' : user_email
        }
    
    return render(request, 'dashboard/settings.html', context=context)
    

   