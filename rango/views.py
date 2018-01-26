from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    html = "Rango says hey there partner!" + "  " '<a href="/rango/about/">about</a>'
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, "rango/index.html", context=context_dict)
    return HttpResponse(html)

def about(request):
    html = "This tutorial has been put together by Stuart McMillan" + "  " + '<a href="/rango/">index</a>'
    context_d = {"boldmessage": "Template using boldmessage"}
    return render(request, "rango/about.html", context=context_d)
    return HttpResponse(html)
