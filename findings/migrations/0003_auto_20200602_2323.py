# Generated by Django 2.2.12 on 2020-06-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findings', '0002_auto_20200306_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='finding',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='rawfinding',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
