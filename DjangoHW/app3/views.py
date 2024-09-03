import datetime

from django.shortcuts import render
from app2.models import User, Product, Order


def index(request):
    return render(request, 'app3/basic.html')


def get_orders(request, pk: int, days=7):
    date = datetime.datetime.now() - datetime.timedelta(minutes=60*24*days)
    orders = Order.objects.filter(customer__pk=pk).filter(date_ordered__gte=date)
    context = {'orders': orders, 'pk': pk, 'day': days}
    print(orders)
    return render(request, 'app3/get_order.html', context=context)


def get_product_in_orders(request, pk: int, days):
    date = datetime.datetime.now() - datetime.timedelta(minutes=60*24*days)
    orders = Order.objects.filter(customer__pk=pk).filter(date_ordered__gte=date)
    products = set()
    for order in orders:
        for pr in order.products.all():
            products.add(pr)
    context = {'orders': products, 'pk': pk, 'day': days}

    return render(request, 'app3/get_prod_in_order.html', context=context)



