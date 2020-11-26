from django_seed import Seed
import random
from django.core.management.base import BaseCommand
from articles.models import Article
from accounts.models import User
from movies.models import Movie


class Command(BaseCommand):

    help = 'This command creates articles, comments'

    def add_arguments(self, parser):
        parser.add_argument (
            '--number', default=1, type=int, help ="How many articles do you want to create?"
        )

    def handle(self, *args, **options):
        all_user = User.objects.all()
        all_movie = Movie.objects.all()

        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(Article, number, {
            'movie' : lambda x: random.choice(all_movie),
            'user' : lambda x: random.choice(all_user),
            'content' : lambda x: seeder.faker.text(),
            'rank' : lambda x: random.randint(0, 5),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} articles created!'))