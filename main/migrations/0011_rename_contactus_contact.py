# Generated by Django 3.2.5 on 2021-08-05 05:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_contactus_usr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactUs',
            new_name='contact',
        ),
    ]
