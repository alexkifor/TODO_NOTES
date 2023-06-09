from django.core.management.base import BaseCommand
# from userapp.models import User
from users.models import User


class Command(BaseCommand):
    help = 'Create Superuser and some test users'

    def add_arguments(self, parser):
        parser.add_argument('count',  nargs='?', type=int, default=5)

    def handle(self, *args, **options):
        # Удаляем все пользоватлелей
        User.objects.all().delete()
        user_count = options['count']
        # Создаем суперпользователя
        User.objects.create_superuser('admin', 'admin@email.com', 'admin')
        # Создаем тестовых пользователей
        for i in range(user_count):
            User.objects.create_user(f'user_{i}', f'user{i}@test.com', 'user')

        print('done')