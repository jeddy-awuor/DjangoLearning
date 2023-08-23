from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def myabout(request):
    return render(request, 'about.html')


def mycontact(request):
    return render(request, 'contactus.html')