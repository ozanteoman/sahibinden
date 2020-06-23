# Generated by Django 2.2.13 on 2020-06-23 22:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
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
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ExteriorFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Frontal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='InteriorFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Landscape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SuitableForDisabled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.City')),
            ],
        ),
        migrations.CreateModel(
            name='NeighborHood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.Town')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertiseAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_detail', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('advertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='advertise.Advertise')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.City')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.NeighborHood')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.Town')),
            ],
        ),
        migrations.AddField(
            model_name='advertise',
            name='exterior_feature',
            field=models.ManyToManyField(to='advertise.ExteriorFeature'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='frontal',
            field=models.ManyToManyField(to='advertise.Frontal'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='interior_feature',
            field=models.ManyToManyField(to='advertise.InteriorFeature'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='landscape',
            field=models.ManyToManyField(to='advertise.Landscape'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='locality',
            field=models.ManyToManyField(to='advertise.Locality'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='sutiable_for_disabled',
            field=models.ManyToManyField(to='advertise.SuitableForDisabled'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='transportation',
            field=models.ManyToManyField(to='advertise.Transportation'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthday', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
