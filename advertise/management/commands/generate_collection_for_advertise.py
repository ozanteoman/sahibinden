from django.core.management import BaseCommand
from advertise.models import Frontal, InteriorFeature, ExteriorFeature, Locality, Transportation, Landscape, SuitableForDisabled


class Command(BaseCommand):

    def _create_collection(self, model_class, items):
        for item in items:
            model_class.objects.create(name=item)

    def handle(self, *args, **options):
        frontal_values = ["Batı", "Doğu", "Güney", "Kuzey"]

        interior_feature = [
            "ADSL", "Ahşap Doğrama", "Akıllı Ev", "Alarm(Hırsız)", "Alarm(Yangın)",
            "Alaturka Tuvalet", "Alüminyum Doğrama", "Amerikan Kapı", "Amerikan Mutfak",
            "Ankastre Fırın", "Asansör", "Balkon", "Barbekü", "Beyaz Eşya", "Bulaşık Makinesi",
            "Duşakabin", "Ebeveyn Banyosu", "Fiber İnternet", "Fırın", "Giyinme Odası", "Görüntülü Diafon",
            "Çelik Kapı", "Şömine"]

        exterior_feature = [
            "Asansör", "Buhar Odası", "Güvenlik", "Hamam", "Hidrofor", "Isı Yalıtım", "Jeneratör", "Kablo TV", "Kamera Sistemi",
            "Kapalı Garaj", "Kapıcı", "Kreş", "Otopark", "Oyun Parkı", "Sauna", "Ses Yalıtımı", "Spor Alanı", "Su Deposu", "Tenis Kortu",
            "Uydu", "Yangın Merdiveni", "Yüzme Havuzu(Açık)", "Yüzme Havuzu(Kapalı)"
        ]

        locality = [
            "Alışveriş Merkezi", "Belediye", "Cami", "Cemevi", "Denize Sıfır", "Eczane", "Eğlence Merkezi", "Fuar",
            "Hastane", "Havra", "Kilise", "Lise", "Market", "Park", "Polis Merkezi", "Sağlık Ocağı", "Semt Pazarı",
            "Spor Salonu", "Üniversite", "İlkokul-Ortaokul", "İtfaiye", "Şehir Merkezi"
        ]

        transportation = [
            "Anayol", "Avrasya Tüneli", "Boğaz Köprüleri", "Cadde", "Deniz Otobüsü", "Dolmuş", "E-5",
            "Havaalanı", "Marmaray", "Metro", "Metrobüs", "Minibüs", "Otobüs Durağı", "Sahil", "TEM",
            "Teleferik", "Tramvay", "Tren İstasyonu", "İskele"
        ]

        landscape = ["Boğaz", "Deniz", "Doğa", "Göl", "Havuz", "Park & Yeşil Alan", "Şehir"]

        suitable_for_disabled = [
            "Araç Park Yeri", "Asansör", "Banyo", "Geniş Koridor", "Giriş / Rampa", "Merdiven", "Mutfak", "Oda Kapısı", "Park",
            "Priz / Elektrik Anahtarı", "Tutamak / Korkuluk", "Tuvalet", "Yüzme Havuzu"
        ]

        self._create_collection(Frontal, frontal_values)
        self._create_collection(InteriorFeature, interior_feature)
        self._create_collection(ExteriorFeature, exterior_feature)
        self._create_collection(Locality, locality)
        self._create_collection(Transportation, transportation)
        self._create_collection(Landscape, landscape)
        self._create_collection(SuitableForDisabled, suitable_for_disabled)
