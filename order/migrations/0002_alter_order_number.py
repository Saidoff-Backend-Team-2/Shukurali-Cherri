# Generated by Django 4.1 on 2024-08-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(max_length=20, unique=True, verbose_name='order number'),
        ),
    ]
