# Generated by Django 5.0 on 2024-04-17 03:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("beers", "0003_beer_label"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="beer",
            options={"permissions": [("special_status", "Can read all beers")]},
        ),
    ]
