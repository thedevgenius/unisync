# Generated by Django 5.1.6 on 2025-03-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_student_guardian_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uni_roll',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='University Roll Number'),
        ),
    ]
