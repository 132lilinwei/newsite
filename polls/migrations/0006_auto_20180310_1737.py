# Generated by Django 2.0.2 on 2018-03-10 09:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180309_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 10, 9, 37, 57, 654062, tzinfo=utc), verbose_name='date published'),
        ),
    ]
