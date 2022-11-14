from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "home.html", {'name':'Denzel'})

def calculate(request):
    val = request.GET['value']
    return render(request, "results.html", {'result':val})

