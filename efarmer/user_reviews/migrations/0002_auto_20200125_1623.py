# Generated by Django 2.2.8 on 2020-01-25 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreviews',
            old_name='views',
            new_name='stars',
        ),
    ]
