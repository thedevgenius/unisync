# Generated by Django 5.1.6 on 2025-03-05 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_course'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.course')),
                ('particular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.particular')),
            ],
            options={
                'ordering': ['due_date'],
                'unique_together': {('due_date', 'particular', 'course')},
            },
        ),
    ]
