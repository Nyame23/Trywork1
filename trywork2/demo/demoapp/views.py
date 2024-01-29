from django.shortcuts import render


def hi(request):
    return render(request, 'demoapp/hi.html')


def home(request):
    return render(request, 'demoapp/home.html')


def about(request):
    return render(request, 'demoapp/about.html')
