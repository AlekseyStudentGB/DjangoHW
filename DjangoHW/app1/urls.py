from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.hi, name='hi'),
    path('about/', views.about, name='about'),
]
