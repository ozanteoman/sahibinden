from django.db import models

from advertise.choices import (NumberOfRoomsChoices,
                               NumberOfBuildingAgeChoices,
                               NumberOfFloorChoices,
                               NumberOfBathroomsChoices,
                               HeatingChoices,
                               UsingStatusChoices,
                               AdvertiseStatusChocies,
                               AdvertiseVisibilityChoices
                               )


class Advertise(models.Model):
    owner = models.ForeignKey(to="advertise.User", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField(default=0)
    square_meter = models.PositiveIntegerField(default=0)
    number_of_rooms = models.PositiveIntegerField(choices=NumberOfRoomsChoices.CHOICES)
    building_age = models.PositiveIntegerField(choices=NumberOfBuildingAgeChoices.CHOICES)
    floor = models.PositiveIntegerField(choices=NumberOfFloorChoices.FLOOR_CHOICES)
    number_of_floors = models.PositiveIntegerField(choices=NumberOfFloorChoices.FLOORS_CHOICES)
    number_of_bathrooms = models.PositiveIntegerField(choices=NumberOfBathroomsChoices.CHOICES)
    heating = models.PositiveIntegerField(choices=HeatingChoices.CHOICES)
    balcony_exists = models.BooleanField(default=False)
    using_status = models.PositiveIntegerField(choices=UsingStatusChoices.CHOICES)
    fee = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=AdvertiseStatusChocies.CHOICES)
    visibility = models.PositiveIntegerField(choices=AdvertiseVisibilityChoices.CHOICES)

    # collections
    frontal = models.ManyToManyField(to="advertise.Frontal")
    interior_feature = models.ManyToManyField(to="advertise.InteriorFeature")
    exterior_feature = models.ManyToManyField(to="advertise.ExteriorFeature")
    locality = models.ManyToManyField(to="advertise.Locality")
    transportation = models.ManyToManyField(to="advertise.Transportation")
    landscape = models.ManyToManyField(to="advertise.Landscape")
    sutiable_for_disabled = models.ManyToManyField(to="advertise.SuitableForDisabled")

    def __str__(self):
        return f"{self.title}"
