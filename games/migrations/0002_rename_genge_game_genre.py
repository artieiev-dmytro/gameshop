# Generated by Django 3.2.17 on 2023-02-04 21:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="genge",
            new_name="genre",
        ),
    ]
