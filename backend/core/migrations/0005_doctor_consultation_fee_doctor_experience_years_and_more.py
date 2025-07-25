# Generated by Django 5.2.3 on 2025-07-19 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='consultation_fee',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience_years',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(blank=True, help_text='e.g., MD, MBBS, PhD', max_length=255),
        ),
        migrations.AddField(
            model_name='doctor',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
