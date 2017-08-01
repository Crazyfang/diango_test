from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    # return render(request, 'home.html', context)
    # return render(request, 'people/home.html')
    return HttpResponse('test words')
