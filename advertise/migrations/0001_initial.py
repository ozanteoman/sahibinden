# Generated by Django 2.2.13 on 2020-06-11 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.PositiveIntegerField(default=0)),
                ('square_meter', models.PositiveIntegerField(default=0)),
                ('number_of_rooms', models.PositiveIntegerField(choices=[(0, '1+0'), (1, '1+1'), (2, '2+0'), (3, '2+1'), (4, '2+2'), (5, '3+1'), (6, '3+2'), (7, '4+1'), (8, '4+2'), (9, '5+1'), (10, '5+2')])),
                ('building_age', models.PositiveIntegerField(choices=[(0, '1'), (1, '2'), (2, '3'), (3, '4'), (4, '5-10 Arası'), (5, '11-15 Arası'), (6, '16-20 Arası')])),
                ('floor', models.PositiveIntegerField(choices=[(0, 'Bodrum Kat'), (1, 'Zemin Kat'), (2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5'), (7, '6'), (8, '7'), (9, '8'), (10, '9'), (11, '10'), (12, '11'), (13, '12'), (14, '13'), (15, '14'), (16, '15')])),
                ('number_of_floors', models.PositiveIntegerField(choices=[(2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5'), (7, '6'), (8, '7'), (9, '8'), (10, '9'), (11, '10'), (12, '11'), (13, '12'), (14, '13'), (15, '14'), (16, '15')])),
                ('number_of_bathrooms', models.PositiveIntegerField(choices=[(0, 'Yok'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('heating', models.PositiveIntegerField(choices=[(0, 'Yok'), (1, 'Soba'), (2, 'Doğalgaz Sobası'), (3, 'Kat Kaloriferi'), (4, 'Merkezi Isıtıcı'), (5, 'Doğalgaz'), (6, 'Klima'), (7, 'Şömine')])),
                ('balcony_exists', models.BooleanField(default=False)),
                ('using_status', models.PositiveIntegerField(choices=[(0, 'Boş'), (1, 'Kiracılı'), (2, 'Mülk Sahibi')])),
                ('fee', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Aktif'), (1, 'Silinmiş')])),
                ('visibility', models.PositiveIntegerField(choices=[(0, 'Herkes'), (1, 'Sadece Ben')])),
            ],
        ),
    ]
