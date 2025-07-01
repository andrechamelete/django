from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import ApplicationForm, InputForm, LogForm

def home(request): 
    path = request.path 
    method = request.method 
    name = "Andre"
    content= f''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : {path}</p> 
<p>Request Method :{method}</p>
<p>nome: {name}</p></center> 
'''
    return HttpResponse(content) 

def date(request):
    date_joined = datetime.today().isoformat()
    return HttpResponse(date_joined)

def home(request):
    text = """<h1 style="color: #F4CE14;">This is Little Lemon again</h1>"""
    return HttpResponse(text)

def showForm(request): 
    form = ApplicationForm(request.POST) 
    return render(request, 'form.html', {'form': form}) 

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)

def form_v(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)