import decimal

from django.core.management import BaseCommand
from app2.models import Order, User, Product
from random import randint, choice, choices
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'the command to create orders'

    def handle(self, *args, **options):
        user = choice(User.objects.all())
        product = choices(Product.objects.all(), k=5)
        order = Order(
                    customer=user,

                    total_price=randint(101, 9999)/100
                )

        order.save()
        for prod in product:
            order.products.add(prod)

        self.stdout.write(f'создано  заказов')
