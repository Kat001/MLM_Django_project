# Generated by Django 3.0.4 on 2020-05-15 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Requested_Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('date', models.DateField(default='1999-01-01')),
                ('fund', models.IntegerField(default=0)),
                ('transection_no', models.IntegerField(default=0)),
                ('proof', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('status', models.CharField(default='Pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tree_View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=50, unique=True)),
                ('left', models.CharField(default='null', max_length=50)),
                ('right', models.CharField(default='null', max_length=50)),
                ('left_count', models.IntegerField(default=0)),
                ('right_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ROI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=20)),
                ('date', models.DateField(default='1999-01-01')),
                ('income', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phon_no', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('package', models.IntegerField(default=1000)),
                ('is_active', models.BooleanField(default=False)),
                ('active_amount', models.IntegerField(default=0)),
                ('sponsor_id', models.CharField(default='null', max_length=50)),
                ('side', models.CharField(default='null', max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avail_fund', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
