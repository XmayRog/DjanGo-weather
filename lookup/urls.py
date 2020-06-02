
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about.htm', views.about, name="about"),
]
