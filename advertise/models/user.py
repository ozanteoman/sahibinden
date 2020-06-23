from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, null=True)

    class Meta:
        verbose_name = "User"
