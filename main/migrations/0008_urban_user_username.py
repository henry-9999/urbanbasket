# Generated by Django 5.2.4 on 2025-07-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_latest_produce_urban_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='urban_user',
            name='username',
            field=models.CharField(default=''),
        ),
    ]
