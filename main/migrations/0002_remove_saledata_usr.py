# Generated by Django 3.2.5 on 2021-07-29 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saledata',
            name='usr',
        ),
    ]
