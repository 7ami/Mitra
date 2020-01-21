from django.shortcuts import render, HttpResponse
from .models import Accommo
from math import ceil
# Create your views here.


def accommo(request):
    everyprod = []
    catprods = Accommo.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prods = Accommo.objects.filter(category=cat)
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        everyprod.append([prods, range(1, nSlides), nSlides])

    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # everyprod = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allProds': everyprod}
    return render(request, 'companies/accommo.html', params)


def home(request):
    return render(request, 'companies/home.html')
 # django automatically takes id iff nott mentioned primary key


def hotelview(request, myid):
    product = Accommo.objects.filter(id=myid)
    return render(request, 'companies/hotelview.html', {'product': product[0]})


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


def guide(request):
    return render(request, 'companies/guide.html')
