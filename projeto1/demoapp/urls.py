from django.urls import path
from . import views

app_name = 'demoapp'

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('date/', views.date),
    path("form/", views.showForm, name="Form"),
    path("homepage/", views.form_view, name="homepage"),
    path("form_v/", views.form_v, name="form_v"),
]