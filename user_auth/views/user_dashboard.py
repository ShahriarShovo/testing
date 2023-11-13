from django.shortcuts import render


def user_dashboard(request):
    return render(request,'dashboard/user_dashboard.html')


