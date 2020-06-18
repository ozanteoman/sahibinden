from django.contrib import admin

from advertise.models import (Advertise,
                              SuitableForDisabled,
                              Landscape,
                              Transportation,
                              Locality,
                              ExteriorFeature,
                              InteriorFeature,
                              Frontal,
                              City,
                              Town,
                              NeighborHood,
                              AdvertiseAddress)

admin.site.register(Advertise)
admin.site.register(SuitableForDisabled)
admin.site.register(Landscape)
admin.site.register(Transportation)
admin.site.register(Locality)
admin.site.register(ExteriorFeature)
admin.site.register(InteriorFeature)
admin.site.register(Frontal)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(NeighborHood)
admin.site.register(AdvertiseAddress)
