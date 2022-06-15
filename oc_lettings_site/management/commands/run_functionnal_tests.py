import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Launch the functionnal tests on the live server'

    def handle(self, *args, **kwargs):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
        os.system('python oc_lettings_site/tests/test_fonctionnal.py')

