# Generated by Django 3.0.2 on 2020-08-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapplication', '0003_auto_20200824_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eimage',
            field=models.FileField(upload_to='static/upload/'),
        ),
    ]
