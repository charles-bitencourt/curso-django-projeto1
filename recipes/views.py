from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_view(request):
    return render(request, 'recipes/home.html', context={'name': 'Charles'})
