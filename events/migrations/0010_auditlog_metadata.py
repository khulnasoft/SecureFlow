# Generated by Django 2.2.14 on 2020-07-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auditlog_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='metadata',
            field=models.TextField(default='n/a'),
        ),
    ]
