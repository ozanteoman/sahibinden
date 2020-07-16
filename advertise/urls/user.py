from django.urls import path

from advertise.views.user import retrieve

urlpatterns = [
    path('<str:username>', view=retrieve, name="retrieve")
]
