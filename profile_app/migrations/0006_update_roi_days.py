# Generated by Django 3.0.4 on 2020-06-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0005_bank_info_cheak'),
    ]

    operations = [
        migrations.AddField(
            model_name='update_roi',
            name='days',
            field=models.IntegerField(default=30),
        ),
    ]