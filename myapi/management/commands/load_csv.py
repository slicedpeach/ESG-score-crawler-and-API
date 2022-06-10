
from csv import DictReader
from django.core.management import BaseCommand

from myapi.models import Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        records = Company.objects.all()
        records.delete()
        # Show this if the data already exist in the database
        if Company.objects.exists():
            print('company data already loaded...exiting.')
            return

        # Show this before loading the data into the database
        print("Loading Companies' data")

        # Code to load the data into database
        for row in DictReader(open('./esgscores.csv')):
            comp = Company(
                name=row['name'], ric = row['ric'],rank=str(row['rank']), esgscore=row['esg'], environmental=row['environmental'], social=row['social'], governance=row['governance'])
            comp.save()
        print("data loaded into api!")
