# Generated by Django 3.2.19 on 2023-06-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_implementation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementation',
            name='no_of_days',
            field=models.DurationField(blank=True),
        ),
    ]
