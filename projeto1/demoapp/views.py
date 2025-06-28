from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request): 
    path = request.path 
    method = request.method 
    name = "Andre"
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p>
<p>nome: {}</p></center> 
'''.format(path, method, name) 
    return HttpResponse(content) 

def homepage(request):
    return HttpResponse('<h1>Welcome to Little Lemon</h1>')

def date(request):
    date_joined = datetime.today().month
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;">This is Little Lemon again</h1>"""
    return HttpResponse(text)