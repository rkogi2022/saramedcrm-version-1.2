# Generated by Django 3.2.19 on 2023-06-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='business_prospect',
            fields=[
                ('lead_id', models.AutoField(primary_key=True, serialize=False)),
                ('facility_name', models.CharField(max_length=300)),
                ('county', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.TextField(blank=True)),
                ('created_date', models.DateField()),
                ('feedback', models.TextField(blank=True)),
                ('feedback_timestamp', models.DateField(blank=True, null=True)),
            ],
        ),
    ]