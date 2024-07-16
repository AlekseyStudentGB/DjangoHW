import datetime

from django.shortcuts import render
from app2.models import User, Product, Order


def get_orders(request, pk: int, days=7):
    date = datetime.datetime.now() - datetime.timedelta(minutes=60*24*days)
    orders = Order.objects.filter(customer__pk=pk).filter(date_ordered__gte=date)
    context = {'orders': orders, 'pk': pk, 'day': days}
    print(orders)
    return render(request, 'get_order.html', context=context)

