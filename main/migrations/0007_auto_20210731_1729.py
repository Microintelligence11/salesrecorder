# Generated by Django 3.2.5 on 2021-07-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210731_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expancedata',
            name='buyerName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expancedata',
            name='buyerPhone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='expancedata',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expancedata',
            name='serviceName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='cosName',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='serviceName',
            field=models.CharField(max_length=100),
        ),
    ]