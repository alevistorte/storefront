from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Request handler


def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    #     pass

    products = Product.objects.filter(unit_price__range=(20, 30))

    return render(request, 'hello.html', {'name': 'Alejandro', 'products': list(products)})
    # return HttpResponse(product)
