from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    html = "Rango says hey there partner!" + "  " '<a href="/rango/about/">about</a>'
    return HttpResponse(html)

def about(request):
    html = "Rango says here is the about page." + "  " + '<a href="/rango/">index</a>'
    return HttpResponse(html)
