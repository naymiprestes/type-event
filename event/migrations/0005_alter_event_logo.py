# Generated by Django 4.2 on 2023-05-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_rename_cor_segundaria_event_cor_secundaria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=models.ImageField(upload_to='logos'),
        ),
    ]
