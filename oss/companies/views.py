from django.shortcuts import render, HttpResponse
# Create your views here.


def home(request):
    return render(request, 'companies/home.html')


def tour(request):
    return render(request, 'companies/tour.html')
