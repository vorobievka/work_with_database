import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

        for phone in phones:
            # TODO: Добавьте сохранение модели
            print(phone.get('name'))
            Phone(name=phone.get('name'), price=phone.get('price'), image=phone.get('image'),
                  release_date=phone.get('release_date'), lte_exists=phone.get('lte_exists')).save()
