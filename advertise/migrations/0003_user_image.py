# Generated by Django 2.2.13 on 2020-08-13 20:51

import advertise.helpers.upload_to
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0002_auto_20200624_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=advertise.helpers.upload_to.upload_to_user),
        ),
    ]
