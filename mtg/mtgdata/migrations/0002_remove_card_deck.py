# Generated by Django 3.0.5 on 2020-04-02 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtgdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='deck',
        ),
    ]
