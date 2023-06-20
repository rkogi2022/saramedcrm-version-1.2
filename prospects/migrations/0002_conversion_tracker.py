# Generated by Django 3.2.19 on 2023-06-14 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prospects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='conversion_tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demostatus', models.CharField(choices=[('DONE', 'DONE'), ('PENDING', 'PENDING')], default='PENDING', max_length=30)),
                ('demodate', models.DateField(blank=True, default=None, null=True)),
                ('Attendees', models.TextField(blank=True)),
                ('meeting', models.CharField(blank=True, choices=[('PHYSICAL', 'PHYSICAL'), ('VIRTUAL', 'VIRTUAL')], max_length=30)),
                ('feedback', models.TextField(blank=True)),
                ('assessmentdate', models.DateField(blank=True, default=None, null=True)),
                ('report', models.FileField(blank=True, upload_to='documents/')),
                ('reportdate', models.DateField(blank=True, default=None, null=True)),
                ('expression', models.FileField(blank=True, upload_to='documents/')),
                ('facility_license', models.FileField(blank=True, upload_to='documents/')),
                ('krapin', models.FileField(blank=True, upload_to='documents/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('demo_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prospects.business_prospect')),
            ],
        ),
    ]