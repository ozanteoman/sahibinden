from django.db import models


class Frontal(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class InteriorFeature(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class ExteriorFeature(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Transportation(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Landscape(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class SuitableForDisabled(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
