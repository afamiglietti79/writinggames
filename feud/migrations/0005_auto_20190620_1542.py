# Generated by Django 2.2.2 on 2019-06-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feud', '0004_feudballot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='is_accepting_votes',
            field=models.IntegerField(default=0),
        ),
    ]
