from django.shortcuts import render, HttpResponse
# Create your views here.


def home(request):
    return render(request, 'companies/home.html')


def tour(request):
    return render(request, 'companies/tour.html')


def aptaxi(request):
    return render(request, 'companies/aptaxi.html')


def dinning(request):
    return render(request, 'companies/dinning.html')


def token(request):
    return render(request, 'companies/token.html')


def ticket(request):
    return render(request, 'companies/ticket.html')


def accommo(request):
    return render(request, 'companies/accommo.html')


def guide(request):
    return render(request, 'companies/guide.html')
