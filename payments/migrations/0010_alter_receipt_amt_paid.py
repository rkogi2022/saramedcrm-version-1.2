# Generated by Django 3.2.19 on 2023-06-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_auto_20230622_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='amt_paid',
            field=models.PositiveIntegerField(),
        ),
    ]
