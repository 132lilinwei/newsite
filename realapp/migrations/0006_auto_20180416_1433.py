# Generated by Django 2.0.3 on 2018-04-16 06:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0005_auto_20180403_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='geolocation',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='tried',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 6, 33, 27, 144908, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='digicard',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]