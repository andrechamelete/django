from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('homepage/', views.homepage),
    path('date/', views.date),
    path('menu/', views.menu)
]