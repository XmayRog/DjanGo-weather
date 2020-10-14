from django.shortcuts import render
import json
import requests

# Create your views here.

def home(request):

    if request.method ==  "POST":
        pincode = request.POST['pincode']


        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + pincode + ",in&appid=e5eca5026398b5afdcb93c955e447dd7&units=metric&lang=en")

        try:
            api = json.loads(api_request.content)


        except Exception as e:
            api = "Error..."

        return render(request, 'home.htm', {'api': api})
    else:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=' + pincode + ',in&appid=e5eca5026398b5afdcb93c955e447dd7&units=metric&lang=en")

        try:
            api = json.loads(api_request.content)


        except Exception as e:
            api = "Error..."


        return render(request, 'home.htm', {'api': api})


def about(request):
    return render(request, 'about.htm', {})
