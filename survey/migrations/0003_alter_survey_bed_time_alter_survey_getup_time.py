# Generated by Django 4.1.1 on 2022-11-08 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0002_basicinfo_gender_basicinfo_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="survey", name="bed_time", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="survey", name="getup_time", field=models.IntegerField(),
        ),
    ]
