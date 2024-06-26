# Generated by Django 4.2.13 on 2024-05-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("original_name", models.CharField(max_length=255)),
                ("rembg_name", models.CharField(max_length=255)),
                ("image_data", models.BinaryField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
