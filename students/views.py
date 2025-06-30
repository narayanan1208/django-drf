from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return HttpResponse("<h2>Student data</h2>")
