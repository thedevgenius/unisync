# Generated by Django 5.1.6 on 2025-03-05 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
