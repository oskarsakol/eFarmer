# Generated by Django 2.2.8 on 2020-01-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_auto_20200120_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='delivery_address',
        ),
    ]
