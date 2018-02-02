from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
    html = "Rango says hey there partner!" + "  " '<a href="/rango/about/">about</a>'
    return render(request, 'rango/index.html', context_dict)
    return HttpResponse(html)

def about(request):
    html = "This tutorial has been put together by Stuart McMillan" + "  " + '<a href="/rango/">index</a>'
    context_d = {"boldmessage": "This tutorial has been put together by Stuart McMillan"}
    return render(request, "rango/about.html", context=context_d)
    return HttpResponse(html)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
