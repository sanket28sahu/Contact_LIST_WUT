# Generated by Django 3.0.2 on 2020-08-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapplication', '0002_employee_eimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eimage',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
