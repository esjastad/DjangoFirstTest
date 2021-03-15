from django.shortcuts import render

# Create your views here.
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return render(request, "basic/home.html")

def about(request):
    return render(request, "basic/about.html")

def contact(request):
    return render(request, "basic/contact.html")
