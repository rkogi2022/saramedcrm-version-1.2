# Generated by Django 3.2.19 on 2023-06-16 06:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0004_alter_implementation_no_of_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='support',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('logdate', models.DateField(default=django.utils.timezone.now)),
                ('module', models.CharField(choices=[('PATIENT REGISTER', 'PATIENT REGISTER'), ('NURSE', 'NURSE'), ('DOCTOR', 'DOCTOR'), ('LABORATORY', 'LABORATORY'), ('RADIOGRAPHY', 'RADIOGRAPHY'), ('INPATIENT', 'INPATIENT'), ('PHARMACY', 'PHARMACY'), ('CASHIER', 'CASHIER'), ('INVENTORY', 'INVENTORY'), ('FINANCE', 'FINANCE'), ('HUMAN RESOURCE', 'HUMAN RESOURCE'), ('SYSTEM ADMIN', 'SYSTEM ADMIN')], default='PATIENT REGISTER', max_length=30)),
                ('problem', models.TextField(blank=True, null=True)),
                ('solution', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING ', 'PENDING'), ('DONE', 'DONE')], default='PENDING', max_length=20)),
                ('completiondate', models.DateField(blank=True, null=True)),
                ('facility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.implementation')),
            ],
        ),
        migrations.CreateModel(
            name='director',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('logdate', models.DateField(default=django.utils.timezone.now)),
                ('feedback_given', models.TextField(blank=True, null=True)),
                ('facility_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.implementation')),
            ],
        ),
        migrations.CreateModel(
            name='courtesy',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('logdate', models.DateField(default=django.utils.timezone.now)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('facility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.implementation')),
            ],
        ),
    ]
