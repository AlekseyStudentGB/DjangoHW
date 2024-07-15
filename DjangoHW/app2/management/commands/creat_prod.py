import decimal

from django.core.management import BaseCommand
from app2.models import Product
from random import randint
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'the command to create products'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, help='the number of users being created')

    def handle(self, *args, **options):
        count = options['count']
        if count is not None:
            for i in range(count):
                product = Product(
                    product_name=f'product{i}',
                    description=get_random_string(100),
                    price=decimal.Decimal(randint(10, 100)/100),
                    count_product=randint(1, 100)

                )
                product.save()
            self.stdout.write(f'создано {count} продуктов')
        else:
            i = randint(100, 999)
            product = Product(
                product_name=f'product{i}',
                description=get_random_string(100),
                price=decimal.Decimal(randint(10, 100) / 10),
                count_product=randint(1, 100)

            )
            product.save()
            self.stdout.write(f'создан 1 пользыватель {product}')
