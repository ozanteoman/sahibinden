from django.contrib.auth.models import AbstractUser
from django.db import models

from advertise.choices import GenderChoices, MartialStatusChoices, EducationalStatusChoices, ProfessionChoices


class Interest(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    gender = models.PositiveIntegerField(null=True, choices=GenderChoices.CHOICES)
    marital_status = models.PositiveIntegerField(null=True, choices=MartialStatusChoices.CHOICES)
    educational_status = models.PositiveIntegerField(null=True, choices=EducationalStatusChoices.CHOICES)
    profession = models.PositiveIntegerField(null=True, choices=ProfessionChoices.CHOICES)
    interests = models.ManyToManyField(to=Interest)

    class Meta:
        verbose_name = "User"

    @property
    def profile_image(self):
        return "/static/img/profile-placeholder.jpg"

    @property
    def info(self):
        full_name = self.get_full_name() or "-"
        birthday = self.birthday or "-"
        gender = self.get_gender_display() or "-"
        marital_status = self.get_marital_status_display() or "-"
        educational_status = self.get_educational_status_display() or "-"
        profession = self.get_profession_display() or "-"
        interests = ", ".join([interest.name for interest in self.interests.all()]) or "-"
        phone_number = self.phone_number or "-"

        context = {
            'username': self.username,
            'full_name': full_name,
            'birthday': birthday,
            'gender': gender,
            'marital_status': marital_status,
            'educational_status': educational_status,
            'profession': profession,
            'interests': interests,
            'phone_number': phone_number
        }

        return context
