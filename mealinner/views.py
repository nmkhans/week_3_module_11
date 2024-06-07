from django.shortcuts import render
from . import views

def home(req):
  return render(req, "index.html")
