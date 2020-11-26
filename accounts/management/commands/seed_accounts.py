from django_seed import Seed
import random
from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):

    help = 'This command creates users'

    def add_arguments(self, parser):
        parser.add_argument (
            '--number', default=1, type=int, help ="How many users do you want to create?"
        )

    def handle(self, *args, **options):
        all_user = User.objects.all()

        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            'username' : lambda x: seeder.faker.name(),
            'is_staff' : False,
            'is_superuser' : False,
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))