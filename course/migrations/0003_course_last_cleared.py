# Generated by Django 2.2.2 on 2019-08-31 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_roll_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='last_cleared',
            field=models.DateField(default=datetime.datetime(2019, 8, 31, 17, 59, 1, 687172, tzinfo=utc)),
        ),
    ]