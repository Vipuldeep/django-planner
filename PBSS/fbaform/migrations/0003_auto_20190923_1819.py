# Generated by Django 2.2.5 on 2019-09-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbaform', '0002_remove_triggers_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Triggers',
        ),
    ]
