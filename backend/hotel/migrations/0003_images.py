# Generated by Django 5.0.3 on 2024-04-03 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel", "0002_delete_cottages_rooms_is_cottage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.TextField()),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotel.rooms"
                    ),
                ),
            ],
        ),
    ]