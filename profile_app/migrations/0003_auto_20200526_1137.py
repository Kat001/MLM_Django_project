# Generated by Django 3.0.4 on 2020-05-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_auto_20200525_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binary_wallet',
            name='b_income',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='binary_wallet',
            name='total_bincome',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='direct_wallet',
            name='d_income',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='direct_wallet',
            name='total_dincome',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fund',
            name='avail_fund',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requested_fund',
            name='fund',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roi_wallet',
            name='r_income',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roi_wallet',
            name='total_rincome',
            field=models.PositiveIntegerField(default=0),
        ),
    ]