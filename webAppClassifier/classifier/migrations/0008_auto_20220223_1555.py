# Generated by Django 3.2.12 on 2022-02-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classifier", "0007_auto_20220223_1430"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("image", models.ImageField(upload_to="img/%Y/%m/%d/")),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Hotel",
        ),
    ]
