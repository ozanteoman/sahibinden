from django.core.management import BaseCommand

from advertise.models import Interest


class Command(BaseCommand):
    help = "created for bulk operation"

    def handle(self, *args, **options):
        interests_list = ["Aile-Çoçuk", "Alışveriş", "Araba", "Kültür Sanat", "Moda", "Oyun", "Sağlıklı Yaşam", "Seyahat", "Spor", "Teknoloji"]
        for interest_name in interests_list:
            Interest.objects.get_or_create(name=interest_name)
