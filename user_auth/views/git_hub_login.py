from django.shortcuts import redirect, HttpResponse
from django.urls import reverse
import requests
from django.contrib.auth import login
from user_auth.models.user import User


GITHUB_CLIENT_ID =''
GITHUB_CLIENT_SECRET =''
#GITHUB_OAUTH_CALLBACK_URL = 'http://localhost:8000/github-callback/'

def github_login(request):
    # Redirect the user to GitHub for authorization
    #github_url = f'https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&scope=user'
    redirect_uri = request.build_absolute_uri(reverse('github_callback'))
    github_url = f'https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={redirect_uri}&scope=user:email'
    print ("----------------",github_url)
    return redirect(github_url)

def github_callback(request):
    code = request.GET.get('code')
    print ("Code -----", code)
    redirect_uri = request.build_absolute_uri(reverse('github_callback'))
    if code:
        payload = {
        'code': code,
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }
        response = requests.post('https://github.com/login/oauth/access_token', data=payload,
                                  headers={'Accept': 'application/json'})
        if response.status_code == 200:
            data = response.json()
            access_token = data['access_token']
            user_response = requests.get('https://api.github.com/user', headers={
                'Authorization': f'Bearer {access_token}',
            })
            if user_response.status_code == 200:
                user_data = user_response.json()
                print ("user info -------",user_data)
                #if user email is none
                if user_data['email']==None:
                    user, created = User.objects.get_or_create(email=user_data['login'], defaults={
                                    'first_name': user_data['name'],
                                    'username' : user_data['login'],
                                    'role' : 2,
                                    'sign_up_platform' : 2,
                                    'is_active' : True,
                                    })
                    login(request,user)
                else:
                    #if user email is not none
                    user, created = User.objects.get_or_create(email=user_data['email'], defaults={
                                    'first_name': user_data['name'],
                                    'username' : user_data['login'],
                                    'role' : 2,
                                    'sign_up_platform' : 2,
                                    'is_active' : True,
                                    # Add other fields from user_info as needed
                                                })
                    login(request,user)
                    
                return redirect('index')
            else:
                return HttpResponse('Failed to fetch user data from GitHub.')
        else:
            return HttpResponse('Failed to fetch user data from GitHub.')

    return HttpResponse('GitHub login failed.')

