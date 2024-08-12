from django.shortcuts import render
from django.http import HttpResponse


def communication(request):
    return HttpResponse('<h1>MErhaba</h1>')