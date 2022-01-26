from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    return render(request, 'geometry/square.html')

def get_circle_area(request, radius: int):
    return render(request, 'geometry/circle.html')

def get_rectangle_area_by_method(request, width: int, height: int):
    redirect_url = reverse("rect", args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square_area_by_method(request, width: int):
    redirect_url = reverse("square", args=(width, ))
    return HttpResponseRedirect(redirect_url)


def get_circle_area_by_method(request, radius: int):
    redirect_url = reverse("circle", args=(radius,))
    return HttpResponseRedirect(redirect_url)