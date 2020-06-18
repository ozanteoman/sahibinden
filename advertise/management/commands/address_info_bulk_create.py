from django.core.management import BaseCommand

from advertise.models import City, Town, NeighborHood


class Command(BaseCommand):
    help = "Created this manage command to insert info of all town,city ,neighborhood into the related models"
    data = {
        "İstanbul": {
            "Ataşehir": ["Aşıkveysel Mh.", "Atatürk Mh.", "İnönü Mh."],
            "Bakırköy": ["Cevizlik Mh.", "Yenimahalle Mh.", "Zeytinlik"],
            "Beşiktaş": ["Dikilitaş Mh.", "Etiler Mh.", "Yıldız Mh."]
        },
        "Ankara": {
            "Akyurt": ["Atatürk Mh.", "Balıkhisar Mh.", "Çam Mh."],
            "Çankaya": ["Ayrancı Mh.", "Aziziye Mh.", "Güzeltep Mh."],
            "Elmadağ": ["İsmetpaşa Mh.", "Kemalpaşa Mh.", "Tatlıca Mh."]
        },
        "İzmir": {
            "Bornova": ["Birlik Mh.", "Serintepe Mh.", "Yeşilova Mh."],
            "Buca": ["Adatepe Mh.", "Atatürk Mh.", "Cumhuriyet Mh."],
            "Çeşme": ["Alaçatı Mh.", "Boyalık Mh.", "Fahrettinpaşa Mh."]
        },
        "Adana": {
            "Aladağ": ["Mansurlu Mh.", "Sinanpaşa Mh.", "Akören Mh."],
            "Ceyhan": ["Hürriyet Mh.", "Mithatpaşa Mh.", "Şahin Özbilen Mh."],
            "Seyhan": ["19 Mayıs Mh.", "Anadolu Mh.", "Beyköy Mh."],
        }
    }

    def handle(self, *args, **options):
        for city_name, v in self.data.items():
            city = City.objects.create(name=city_name)
            for town_name, neighborhood_list in v.items():
                town = Town.objects.create(city=city, name=town_name)
                for neighborhood_name in neighborhood_list:
                    NeighborHood.objects.create(town=town, name=neighborhood_name)
