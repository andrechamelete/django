from django.urls import path
from . import views

app_name = 'demoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('date/', views.date),
    path("form/", views.showForm, name="Form"),
    path("homepage/", views.form_view, name="homepage"),
    path("about/", views.about, name="about"),
    path('menu/', views.menu, name='menu'),
    path('teste/', views.teste, name="teste")
]