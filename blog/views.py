from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("Home")  # Render a template for the homepage

def my_blog(request):
    return HttpResponse("Hello, Blog!")