from django.shortcuts import render


def thank_you(request):
    return render(request,'include/thank_you.html')