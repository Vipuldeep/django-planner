# Generated by Django 2.2.3 on 2019-09-18 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbaform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triggers',
            name='Location',
        ),
    ]
