# Generated by Django 5.1.6 on 2025-03-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='guardian_contact',
            field=models.CharField(max_length=15, null=True, verbose_name="Guardian's Contact"),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_name',
            field=models.CharField(max_length=100, null=True, verbose_name="Guardian's Name"),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_number',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Registration Number'),
        ),
    ]
