# Generated by Django 3.2.19 on 2023-06-22 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_receipt_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='implementation',
            name='county',
        ),
        migrations.RemoveField(
            model_name='implementation',
            name='town',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='invoice',
        ),
    ]