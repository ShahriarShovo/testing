
from django.shortcuts import redirect
from django.urls import reverse
import requests
from django.conf import settings
from django.shortcuts import redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User

FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''



def facebook_login(request):
    # Generate a random state parameter for security.
    state = 'your_random_state_string'

    # Store the state in the session for later verification.
    request.session['facebook_state'] = state

    # Redirect the user to Facebook for login.
    facebook_url = f'https://www.facebook.com/v12.0/dialog/oauth?client_id={FACEBOOK_APP_ID}&redirect_uri={request.build_absolute_uri(reverse("facebook_callback"))}&state={state}&scope=email'
    return redirect(facebook_url)

def facebook_callback(request):
    # Verify the state parameter to prevent CSRF attacks.
    if request.GET.get('state') != request.session.get('facebook_state'):
        return HttpResponse("State parameter mismatch. Possible CSRF attack.")

    # Exchange the Facebook authorization code for an access token.
    code = request.GET.get('code')
    token_url = f'https://graph.facebook.com/v12.0/oauth/access_token?client_id={FACEBOOK_APP_ID}&redirect_uri={request.build_absolute_uri(reverse("facebook_callback"))}&client_secret={FACEBOOK_APP_SECRET}&code={code}'
    response = requests.get(token_url)
    data = response.json()

    if 'error' in data:
        return HttpResponse(f"Error: {data['error']['message']}")

    access_token = data['access_token']

    # Use the access token to fetch user data.
    user_data_url = f'https://graph.facebook.com/v12.0/me?fields=id,email&access_token={access_token}'
    response = requests.get(user_data_url)
    user_data = response.json()

    print("user data-----------------", user_data)

    # Create or update the user in your database using the user_data.
    # Authenticate the user in your Django application.

    return HttpResponse(f"Logged in as {user_data['email']}")























# def facebook_login(request):
#     # Construct the Facebook login URL
#     redirect_uri = request.build_absolute_uri(reverse('facebook_login_callback'))
#     facebook_login_url = f'https://www.facebook.com/v13.0/dialog/oauth?client_id={FACEBOOK_APP_ID}&redirect_uri={redirect_uri}&scope=email'
    
#     return redirect(facebook_login_url)


# def facebook_login_callback(request):
#     code = request.GET.get('code')
    
#     # Exchange the authorization code for an access token
#     redirect_uri = request.build_absolute_uri(reverse('facebook_login_callback'))
#     params = {
#         'client_id': FACEBOOK_APP_ID,
#         'client_secret': FACEBOOK_APP_SECRET,
#         'code': code,
#         'redirect_uri': redirect_uri,
#     }
#     response = requests.get('https://graph.facebook.com/v13.0/oauth/access_token', params=params)
#     data = response.json()
    
#     if 'access_token' in data:
#         access_token = data['access_token']
#         # Fetch user data using the access token
#         user_data = requests.get(f'https://graph.facebook.com/v13.0/me?fields=id,email,name&access_token={access_token}').json()
#         print("User data ------------------", user_data)
        
#         # Check if a user with this email already exists
#         # email = user_data.get('email')
#         # if email:
#         #     user, created = User.objects.get_or_create(email=email)
#         #     if created:
#         #         user.username = user_data.get('name')
#         #         user.save()
#         #'sign_up_platform' : 3
            
#             # Log the user in
#             #login(request, user)
    
#     #return redirect('home')  # Redirect to the home page or any desired page after login

#     return HttpResponse ("okay")
