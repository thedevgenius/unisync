# Generated by Django 5.1.6 on 2025-03-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_academicyear_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicyear',
            name='status',
        ),
        migrations.RemoveField(
            model_name='academicyear',
            name='title',
        ),
        migrations.AddField(
            model_name='academicyear',
            name='end',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='academicyear',
            name='start',
            field=models.CharField(default='', max_length=4),
        ),
    ]
