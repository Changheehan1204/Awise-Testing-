# Generated by Django 4.1.1 on 2022-11-01 21:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BasicInfo",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("user_name", models.TextField()),
                ("email", models.TextField()),
                ("password", models.TextField()),
                ("school_year", models.IntegerField()),
                ("rent", models.IntegerField()),
                ("move_in_date", models.TextField()),
                ("number_of_room", models.IntegerField()),
                ("location", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("getup_time", models.TextField()),
                ("getup_time_w", models.IntegerField()),
                ("bed_time", models.TextField()),
                ("bed_time_w", models.IntegerField()),
                (
                    "social",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("social_w", models.IntegerField()),
                (
                    "academic",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("academic_w", models.IntegerField()),
                (
                    "bring_people",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("bring_people_w", models.IntegerField()),
                (
                    "animal",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("animal_w", models.IntegerField()),
                (
                    "instrument",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("instrument_w", models.IntegerField()),
                (
                    "cleaning",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("cleaning_w", models.IntegerField()),
                (
                    "cook",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("cook_w", models.IntegerField()),
                (
                    "share",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("share_w", models.IntegerField()),
                (
                    "smoke",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("smoke_w", models.IntegerField()),
                (
                    "alcohol",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("alcohol_w", models.IntegerField()),
            ],
        ),
    ]