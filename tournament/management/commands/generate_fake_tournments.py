from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from users.models import CustomUser
from tournament.models import Tournament
from datetime import date
import datetime
class Command(BaseCommand):
    help = 'this command to generate fake tournaments'

    def handle(self, *args, **options):
        user = CustomUser.objects.first()
        seeder = Seed.seeder()
        seeder.add_entity(Tournament, 15)
        seeder.execute()
