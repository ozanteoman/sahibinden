from django.urls import path

from advertise.views.user import retrieve, edit_user

urlpatterns = [
    path('<str:username>', view=retrieve, name="retrieve"),
    path('<str:username>/edit', view=edit_user, name="edit-user")
]
