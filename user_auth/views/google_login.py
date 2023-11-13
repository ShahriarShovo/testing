from django.shortcuts import redirect, HttpResponse
from django.urls import reverse
import requests
from django.contrib.auth import login
from user_auth.models.user import User
from user_auth.models.google_data import Google_Data


GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
#GOOGLE_OAUTH2_REDIRECT_URI = 'http://localhost:8000'




def google_login(request):
    redirect_uri = request.build_absolute_uri(reverse('google_callback'))
    auth_url = f'https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_OAUTH2_CLIENT_ID}&redirect_uri={redirect_uri}&scope=email profile openid'
    return redirect(auth_url)


def google_callback(request):
    code = request.GET.get('code')
    print("Code ------",code)
    redirect_uri = request.build_absolute_uri(reverse('google_callback'))
    token_url = 'https://accounts.google.com/o/oauth2/token'
    payload = {
        'code': code,
        'client_id': GOOGLE_OAUTH2_CLIENT_ID,
        'client_secret': GOOGLE_OAUTH2_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    # Exchange the authorization code for an access token
    response = requests.post(token_url, data=payload)
    token_data = response.json()
    access_token = token_data['access_token']

    # Fetch user information using the access token
    user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()
    

    email = user_info['email']
    username  = email.split('@')[0]
   

    # Here, you can create or authenticate the user based on user_info data
    # You can use user_info['email'] as a unique identifier, for example
    # Redirect to a success page or perform other actions as needed

    print ("user info ===============", user_info)
    save_google_data = Google_Data.objects.get_or_create(user_email=email,
                                                         defaults={
                                                             'google_user_id' : user_info['id'],
                                                             'verified_email' : user_info['verified_email'],
                                                             'user_name' : user_info['name'],
                                                             'user_given_name' : user_info['given_name'],
                                                             'user_family_name' : user_info['family_name'],
                                                             'user_picture' : user_info['picture'],
                                                             'user_language' : user_info['locale'],
                                                             
                                                             
                                                         })
    print ("user email ===============", email)
    

    user, created = User.objects.get_or_create(email=email, defaults={
        'first_name': user_info['given_name'],
        'last_name': user_info['family_name'],
        'username' : username,
        'role' : 2,
        'sign_up_platform' :1,
        'is_active' : True,
        # Add other fields from user_info as needed
    })

    # Log the user in
    login(request, user)

    return redirect('index')

