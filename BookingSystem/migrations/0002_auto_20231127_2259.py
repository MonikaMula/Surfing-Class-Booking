# Generated by Django 3.2.23 on 2023-11-27 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookingSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['surfing_class', 'participant_name']},
        ),
        migrations.AlterModelOptions(
            name='surfingclass',
            options={'ordering': ['date', 'start_time']},
        ),
    ]
