# Generated by Django 5.1.6 on 2025-03-03 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
