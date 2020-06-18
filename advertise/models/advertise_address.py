from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=25)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    town = models.ForeignKey(to=Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AdvertiseAddress(models.Model):
    advertise = models.ForeignKey(to="advertise.Advertise", on_delete=models.CASCADE, related_name="address")
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    town = models.ForeignKey(to=Town, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(to=NeighborHood, on_delete=models.CASCADE)

    address_detail = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.advertise.title
