from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.htm', {})


def about(request):
    return render(request, 'about.htm', {})
