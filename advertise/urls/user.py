from django.urls import path

from advertise.views.user import retrieve

urlpatterns = [
    path('retrieve', view=retrieve, name="retrieve")
]
