# Generated by Django 3.2.5 on 2021-07-31 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_saledata_usr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expancedata',
            name='price',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='price',
            field=models.CharField(default=0, max_length=50),
        ),
    ]