from django.core.management import BaseCommand
from users.models import User
from config.settings import EMAIL


class Command(BaseCommand):
    help = 'создание суперпользователя'

    def handle(self, *args, **options):
        user = User.objects.create(
            email=EMAIL,
            first_name='Admin',
            last_name='Admin',
            is_superuser=True,
            is_staff=True
        )

        user.set_password('123456')
        user.save()
