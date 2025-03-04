# Generated by Django 5.1.6 on 2025-03-02 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='college_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
