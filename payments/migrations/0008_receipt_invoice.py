# Generated by Django 3.2.19 on 2023-06-21 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_implementation_implementation_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='invoice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='payments.invoice'),
        ),
    ]
