# Generated by Django 3.2.12 on 2022-02-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0008_auto_20220223_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%Y/%m/%d/')),
                ('prediction_result', models.CharField(blank=True, default='', max_length=100)),
                ('prediction_feedback', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
