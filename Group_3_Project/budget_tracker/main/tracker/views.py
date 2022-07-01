from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    page = "<html><head><title>test page</title></head><body><h1>Hello World</h1></body></html>"
    return HttpResponse(page)

def Other(request):
    return render(request, "otherPage.html", {"title": "Other Page", "message": "Hello World!"})