from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("HI. this is an index page")

def staff(request):
    return HttpResponse("HI. this is an staff page")