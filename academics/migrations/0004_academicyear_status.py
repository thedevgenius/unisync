# Generated by Django 5.1.6 on 2025-03-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_academicyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicyear',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
