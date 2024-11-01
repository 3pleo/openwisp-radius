# Generated by Django 4.2 on 2024-10-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("openwisp_radius", "0038_clean_fallbackfields"),
    ]

    operations = [
        migrations.AddField(
            model_name="radiusgroup",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                help_text="The Price set for this Radius Group or Plan; made available to down-stream systems",
                max_digits=10,
                verbose_name="plan price",
            ),
        ),
    ]
