# Generated by Django 3.2.12 on 2022-03-04 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("classifier", "0012_auto_20220302_1445"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prediction",
            name="prediction_feedback",
        ),
        migrations.RemoveField(
            model_name="prediction",
            name="prediction_result",
        ),
        migrations.CreateModel(
            name="Result",
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
                (
                    "expected_result",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                ("prediction_feedback", models.BooleanField(blank=True, default=False)),
                (
                    "imagine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classifier.prediction",
                    ),
                ),
            ],
        ),
    ]
