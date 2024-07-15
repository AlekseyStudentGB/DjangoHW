from django.core.management import BaseCommand
from app2.models import User
from random import randint
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'the command to create users'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, help='the number of users being created')

    def handle(self, *args, **options):
        count = options['count']
        if count is not None:
            for i in range(count):
                user = User(
                    user_name=f'user{i}',
                    email=f'user{i}@mail.ru',
                    user_phone=randint(100_000_000, 999_999_999),
                    user_address=get_random_string(40),
                )
                user.save()
            self.stdout.write(f'создано {count} пользователей')
        else:
            i = randint(100, 999)
            user = User(
                user_name=f'user{i}',
                email=f'user{i}@mail.ru',
                user_phone=randint(100_000_000, 999_999_999),
                user_address=get_random_string(40)
            )
            user.save()
            self.stdout.write(f'создан 1 пользыватель {user}')
