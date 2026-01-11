import pymongo
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Ensure unique index on email field in users collection.'

    def handle(self, *args, **options):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['octofit_db']
        result = db['users'].create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS(f'Created unique index: {result}'))
