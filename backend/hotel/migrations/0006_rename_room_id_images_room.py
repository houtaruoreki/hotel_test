# Generated by Django 5.0.3 on 2024-04-09 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hotel", "0005_services"),
    ]

    operations = [
        migrations.RenameField(
            model_name="images",
            old_name="room_id",
            new_name="room",
        ),
    ]